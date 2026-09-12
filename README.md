# Haven Shoes

## Authentication

This site uses Supabase Auth for signup, login, protected account access, and password changes. It works with Live Server and static hosting.

Before testing signup, add your Live Server address (for example, `http://127.0.0.1:5500`) in Supabase: **Authentication → URL Configuration → Redirect URLs**. Add your real domain there before publishing.

The browser config uses only the Supabase publishable key. Never add a secret or service-role key to this project.
