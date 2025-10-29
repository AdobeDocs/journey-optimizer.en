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

# Check if submodule is configured
if ! git config --file .gitmodules --get-regexp path | grep -q ".cursor-agents"; then
    echo "→ Adding submodule..."
    git submodule add https://git.corp.adobe.com/AdobeDocs/CursorAgents.git .cursor-agents
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
    echo "  git submodule add https://git.corp.adobe.com/AdobeDocs/CursorAgents.git .cursor-agents"
    echo "  git submodule update --init --recursive"
    echo ""
    exit 1
fi

