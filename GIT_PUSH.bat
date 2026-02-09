@echo off
echo ========================================
echo Pushing to GitHub Repository
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Removing old .git folder (if exists)...
if exist .git (
    echo Warning: .git folder exists. Please close VS Code/Cursor and pause OneDrive sync, then run this script again.
    pause
    exit /b 1
)

echo Step 2: Initializing git repository...
git init

echo Step 3: Adding remote repository...
git remote add origin https://github.com/Hesham0-0Nasser/prompt-generator.git 2>nul
if errorlevel 1 (
    git remote set-url origin https://github.com/Hesham0-0Nasser/prompt-generator.git
)

echo Step 4: Adding all files...
git add .

echo Step 5: Committing changes...
git commit -m "Initial commit: Accessories Prompt Generator - Desktop app and web interface"

echo Step 6: Setting main branch...
git branch -M main

echo Step 7: Pushing to GitHub...
echo You may be prompted for GitHub credentials (use Personal Access Token, not password)
git push -u origin main

echo.
echo ========================================
echo Done! Check: https://github.com/Hesham0-0Nasser/prompt-generator
echo ========================================
pause
