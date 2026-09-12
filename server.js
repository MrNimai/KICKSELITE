/* Local development server with cookie-based authentication. Run: node server.js */
const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = __dirname;
const PORT = Number(process.env.PORT) || 3000;
const DATA_DIR = path.join(ROOT, 'data');
const USERS_FILE = path.join(DATA_DIR, 'users.json');
const sessions = new Map();
const SESSION_AGE = 1000 * 60 * 60 * 24 * 7;
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.ico': 'image/x-icon' };

function ensureStore() {
    if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR);
    if (!fs.existsSync(USERS_FILE)) fs.writeFileSync(USERS_FILE, '[]\n', 'utf8');
}
function users() { ensureStore(); return JSON.parse(fs.readFileSync(USERS_FILE, 'utf8')); }
function saveUsers(list) { fs.writeFileSync(USERS_FILE, JSON.stringify(list, null, 2) + '\n', 'utf8'); }
function publicUser(user) { return { id: user.id, name: user.name, email: user.email, createdAt: user.createdAt }; }
function hashPassword(password, salt = crypto.randomBytes(16).toString('hex')) {
    return { salt, hash: crypto.scryptSync(password, salt, 64).toString('hex') };
}
function validPassword(password) { return typeof password === 'string' && password.length >= 8 && password.length <= 128; }
function parseCookies(request) {
    return Object.fromEntries((request.headers.cookie || '').split(';').filter(Boolean).map(item => {
        const index = item.indexOf('=');
        return [item.slice(0, index).trim(), decodeURIComponent(item.slice(index + 1))];
    }));
}
function sessionUser(request) {
    const token = parseCookies(request).haven_session;
    const session = token && sessions.get(token);
    if (!session || session.expiresAt < Date.now()) { if (token) sessions.delete(token); return null; }
    return users().find(user => user.id === session.userId) || null;
}
function createSession(response, user) {
    const token = crypto.randomBytes(32).toString('base64url');
    sessions.set(token, { userId: user.id, expiresAt: Date.now() + SESSION_AGE });
    response.setHeader('Set-Cookie', `haven_session=${token}; HttpOnly; SameSite=Lax; Path=/; Max-Age=${SESSION_AGE / 1000}`);
}
function clearSession(request, response) {
    const token = parseCookies(request).haven_session;
    if (token) sessions.delete(token);
    response.setHeader('Set-Cookie', 'haven_session=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0');
}
function reply(response, status, body) {
    response.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
    response.end(JSON.stringify(body));
}
function readBody(request) {
    return new Promise((resolve, reject) => {
        let body = '';
        request.on('data', chunk => { body += chunk; if (body.length > 20000) reject(new Error('Request too large')); });
        request.on('end', () => { try { resolve(body ? JSON.parse(body) : {}); } catch { reject(new Error('Invalid JSON')); } });
    });
}
function invalidOrigin(request) {
    const origin = request.headers.origin;
    return origin && origin !== `http://${request.headers.host}`;
}

async function api(request, response) {
    if (invalidOrigin(request)) return reply(response, 403, { error: 'Invalid request origin.' });
    const route = new URL(request.url, `http://${request.headers.host}`).pathname;
    if (route === '/api/auth/me' && request.method === 'GET') {
        const user = sessionUser(request);
        return reply(response, 200, { user: user ? publicUser(user) : null });
    }
    if (route === '/api/auth/logout' && request.method === 'POST') {
        clearSession(request, response); return reply(response, 200, { ok: true });
    }
    let body;
    try { body = await readBody(request); } catch (error) { return reply(response, 400, { error: error.message }); }
    if (route === '/api/auth/signup' && request.method === 'POST') {
        const name = String(body.name || '').trim();
        const email = String(body.email || '').trim().toLowerCase();
        if (name.length < 2 || name.length > 80) return reply(response, 400, { error: 'Enter a name between 2 and 80 characters.' });
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return reply(response, 400, { error: 'Enter a valid email address.' });
        if (!validPassword(body.password)) return reply(response, 400, { error: 'Password must be 8–128 characters.' });
        const list = users();
        if (list.some(user => user.email === email)) return reply(response, 409, { error: 'An account with this email already exists.' });
        const credentials = hashPassword(body.password);
        const user = { id: crypto.randomUUID(), name, email, passwordHash: credentials.hash, passwordSalt: credentials.salt, createdAt: new Date().toISOString() };
        list.push(user); saveUsers(list); createSession(response, user);
        return reply(response, 201, { user: publicUser(user) });
    }
    if (route === '/api/auth/login' && request.method === 'POST') {
        const email = String(body.email || '').trim().toLowerCase();
        const user = users().find(item => item.email === email);
        if (!user || !validPassword(body.password)) return reply(response, 401, { error: 'Email or password is incorrect.' });
        const candidate = hashPassword(body.password, user.passwordSalt).hash;
        if (!crypto.timingSafeEqual(Buffer.from(candidate, 'hex'), Buffer.from(user.passwordHash, 'hex'))) return reply(response, 401, { error: 'Email or password is incorrect.' });
        createSession(response, user); return reply(response, 200, { user: publicUser(user) });
    }
    if (route === '/api/account' && request.method === 'PATCH') {
        const user = sessionUser(request);
        if (!user) return reply(response, 401, { error: 'Please sign in to continue.' });
        const list = users(); const record = list.find(item => item.id === user.id);
        const name = String(body.name || '').trim(); const email = String(body.email || '').trim().toLowerCase();
        if (name.length < 2 || name.length > 80) return reply(response, 400, { error: 'Enter a name between 2 and 80 characters.' });
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return reply(response, 400, { error: 'Enter a valid email address.' });
        if (list.some(item => item.id !== user.id && item.email === email)) return reply(response, 409, { error: 'That email is already in use.' });
        record.name = name; record.email = email; saveUsers(list); return reply(response, 200, { user: publicUser(record) });
    }
    if (route === '/api/account/password' && request.method === 'POST') {
        const user = sessionUser(request);
        if (!user) return reply(response, 401, { error: 'Please sign in to continue.' });
        if (!validPassword(body.newPassword)) return reply(response, 400, { error: 'New password must be 8–128 characters.' });
        const oldHash = hashPassword(body.currentPassword || '', user.passwordSalt).hash;
        if (!crypto.timingSafeEqual(Buffer.from(oldHash, 'hex'), Buffer.from(user.passwordHash, 'hex'))) return reply(response, 401, { error: 'Current password is incorrect.' });
        const credentials = hashPassword(body.newPassword); const list = users(); const record = list.find(item => item.id === user.id);
        record.passwordHash = credentials.hash; record.passwordSalt = credentials.salt; saveUsers(list);
        return reply(response, 200, { ok: true });
    }
    return reply(response, 404, { error: 'Route not found.' });
}
function serveFile(request, response) {
    const pathname = decodeURIComponent(new URL(request.url, `http://${request.headers.host}`).pathname);
    const requested = pathname === '/' ? 'index.html' : pathname.replace(/^\/+/, '');
    const file = path.resolve(ROOT, requested);
    if (!file.startsWith(ROOT + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { response.writeHead(404); return response.end('Not found'); }
    response.writeHead(200, { 'Content-Type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(response);
}
ensureStore();
http.createServer((request, response) => request.url.startsWith('/api/') ? api(request, response).catch(() => reply(response, 500, { error: 'Server error.' })) : serveFile(request, response)).listen(PORT, () => console.log(`Haven Shoes is running at http://localhost:${PORT}`));
