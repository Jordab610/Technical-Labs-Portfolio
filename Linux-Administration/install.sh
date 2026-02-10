#!/bin/zsh

echo "🚀 Starting environment setup..."

# 1. Grant execution permissions to all .sh and .zsh files
echo "📦 Setting permissions for scripts..."
chmod +x *.sh *.zsh

# 2. Check if GitHub CLI is installed
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI is installed."
else
    echo "⚠️ GitHub CLI not found. Run 'brew install gh' to enable GitHub features."
fi

echo "✨ Setup complete! Your scripts are now executable."
