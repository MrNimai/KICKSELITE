@echo off
title Haven Shoes
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
    echo Node.js is required to run Haven Shoes.
    echo Install the current LTS version from https://nodejs.org then run this file again.
    pause
    exit /b 1
)
netstat -ano | findstr /r /c:":3000 .*LISTENING" >nul
if errorlevel 1 (
    start "Haven Shoes" /b node server.js
    timeout /t 2 /nobreak >nul
)
start "" http://localhost:3000
echo Haven Shoes is running at http://localhost:3000
echo Keep this window open while using sign in and sign up.
pause
