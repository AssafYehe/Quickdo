#!/bin/bash
# GitHub Setup Script for Task Manager

echo "🚀 Task Manager - GitHub Setup"
echo "================================"
echo ""
echo "This script will help you push your task manager to GitHub."
echo ""
read -p "Enter your GitHub username: " github_username
read -p "Enter the repository name (default: task-manager): " repo_name
repo_name=${repo_name:-task-manager}

echo ""
echo "Setting up remote repository..."
git remote add origin "https://github.com/$github_username/$repo_name.git"

echo ""
echo "✓ Git repository is ready!"
echo ""
echo "Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Create a new repository called '$repo_name'"
echo "3. Keep it public (or private if you prefer)"
echo "4. DO NOT initialize with README, .gitignore, or license"
echo "5. Once created, run: git push -u origin main"
echo ""
echo "Or run this command now if you've already created the repo:"
echo "  git push -u origin main"

