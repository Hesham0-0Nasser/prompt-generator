# PowerShell script to push to GitHub
# Run this script in PowerShell: .\push-to-github.ps1

Write-Host "Initializing git repository..." -ForegroundColor Green

# Initialize git if not already done
if (-not (Test-Path .git)) {
    git init
}

# Add remote if not exists
$remoteExists = git remote | Select-String -Pattern "origin"
if (-not $remoteExists) {
    Write-Host "Adding remote repository..." -ForegroundColor Green
    git remote add origin https://github.com/Hesham0-0Nasser/prompt-generator.git
} else {
    Write-Host "Remote already exists, updating..." -ForegroundColor Yellow
    git remote set-url origin https://github.com/Hesham0-0Nasser/prompt-generator.git
}

# Add all files
Write-Host "Adding files..." -ForegroundColor Green
git add .

# Commit
Write-Host "Committing changes..." -ForegroundColor Green
git commit -m "Initial commit: Accessories Prompt Generator - Desktop app and web interface"

# Set main branch
Write-Host "Setting main branch..." -ForegroundColor Green
git branch -M main

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Green
Write-Host "You may be prompted for GitHub credentials." -ForegroundColor Yellow
git push -u origin main

Write-Host "Done! Check your repository at: https://github.com/Hesham0-0Nasser/prompt-generator" -ForegroundColor Green
