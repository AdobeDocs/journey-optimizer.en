#!/bin/bash

# Cursor Agents Setup Script
# This script initializes the git submodule containing shared Cursor agents

set -e  # Exit on error

echo "🚀 Cursor Agents Setup"
echo "===================="
echo ""

# Check if .cursor-agents directory exists
if [ -d ".cursor-agents/agents" ] && [ "$(ls -A .cursor-agents/agents 2>/dev/null)" ]; then
    echo "✅ Cursor Agents are already installed!"
    echo ""
    echo "Available agents:"
    echo "  - @draft-page (Draft Page Generator)"
    echo "  - @fix-grammar (Grammar Fixer)"
    echo ""
    echo "Nothing to do! 🎉"
    exit 0
fi

echo "📦 Installing Cursor Agents..."
echo ""

# Test git access (silently)
echo "→ Testing git access..."

SSH_WORKS=false
HTTPS_WORKS=false

# Test SSH
if git ls-remote git@git.corp.adobe.com:AdobeDocs/CursorAgents.git >/dev/null 2>&1; then
    SSH_WORKS=true
fi

# Test HTTPS
if git ls-remote https://git.corp.adobe.com/AdobeDocs/CursorAgents.git >/dev/null 2>&1; then
    HTTPS_WORKS=true
fi

# Determine which URL to use
if [ "$SSH_WORKS" = true ]; then
    REPO_URL="git@git.corp.adobe.com:AdobeDocs/CursorAgents.git"
    echo "✅ Access verified (SSH)!"
elif [ "$HTTPS_WORKS" = true ]; then
    REPO_URL="https://git.corp.adobe.com/AdobeDocs/CursorAgents.git"
    echo "✅ Access verified (HTTPS)!"
else
    echo ""
    echo "❌ Git Access Not Configured"
    echo ""
    echo "I couldn't access git.corp.adobe.com with your current setup."
    echo ""
    echo "Options:"
    echo "  1. Set up SSH keys: https://git.corp.adobe.com/settings/keys"
    echo "  2. Set up HTTPS token: https://git.corp.adobe.com/settings/tokens"
    echo "  3. Ask your team lead for help"
    echo ""
    echo "After configuring access, run this script again:"
    echo "  ./setup-agents.sh"
    echo ""
    exit 1
fi

# Check if submodule is configured
if ! git config --file .gitmodules --get-regexp path | grep -q ".cursor-agents" 2>/dev/null; then
    echo "→ Adding submodule..."
    git submodule add "$REPO_URL" .cursor-agents
fi

# Initialize submodule
echo "→ Initializing git submodule..."
git submodule init

# Update submodule to latest
echo "→ Fetching latest agents..."
git submodule update --remote --recursive

# Verify installation
if [ -d ".cursor-agents/agents" ] && [ "$(ls -A .cursor-agents/agents 2>/dev/null)" ]; then
    echo ""
    echo "✅ Installation Complete!"
    echo ""
    echo "Installed agents:"
    echo "  - 📄 Draft Page Generator (@draft-page)"
    echo "  - 🎯 Fix Grammar (@fix-grammar)"
    echo ""
    echo "You can now use agents in Cursor. Try typing:"
    echo "  @draft-page"
    echo ""
    echo "Happy documenting! ✨"
else
    echo ""
    echo "❌ Installation Failed"
    echo ""
    echo "The agents directory was not created properly."
    echo "Please check:"
    echo "  1. Your network connection"
    echo "  2. VPN is connected"
    echo "  3. Git access to https://git.corp.adobe.com/AdobeDocs/CursorAgents"
    echo ""
    echo "Try running manually:"
    echo "  git submodule update --init --recursive"
    echo ""
    exit 1
fi

