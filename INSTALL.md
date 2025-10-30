# 🚀 Installing Cursor Agents

Cursor Agents are shared tools that help you create and maintain documentation more efficiently.

## First Time Setup

You only need to do this **once** per repository.

### Option 1: Using Cursor (Recommended ⭐)

1. Open Cursor Chat (`Cmd+L` or `Ctrl+L`)
2. Type:

   ```
   @setup-agents
   ```

3. The agent will automatically:
   - Test SSH and HTTPS access
   - Use the working method
   - Guide you through setup if needed
4. Done! ✨

**Note:** The agent automatically detects if you have SSH or HTTPS access to `git.corp.adobe.com` and uses the appropriate method. If neither works, it provides a guided setup.

### Option 2: Using Terminal

1. Open your terminal in the repository root
2. Run:

   ```bash
   ./setup-agents.sh
   ```

   The script will automatically:
   - Test SSH and HTTPS access
   - Use the working method
   - Show setup instructions if needed

   Or manually (if you know your git is configured):

   ```bash
   git submodule update --init --recursive
   ```

3. Done! ✨

## Verification

After setup, verify the installation:

```bash
ls .cursor-agents/agents/
```

You should see:
- `draft-page-generator.md`
- `fix-grammar.md`
- etc.

## Usage

Once installed, you can use agents in Cursor:

```
@draft-page      # Generate a new documentation page
@fix-grammar     # Fix grammar in current file
```

See [AGENTS.md](AGENTS.md) for full list of available agents.

## Updating Agents

To get the latest version of all agents:

### Option 1: Using Cursor
```
@update-agents
```

### Option 2: Using Terminal
```bash
git submodule update --remote
```

## Troubleshooting

### "Agent not found" error

If you see this error, the agents are not installed yet. Run:
```
@setup-agents
```

### Submodule is empty

If `.cursor-agents/` exists but is empty:
```bash
git submodule update --init --recursive --remote
```

### Permission denied

Make sure the setup script is executable:
```bash
chmod +x setup-agents.sh
```

### Network/VPN issues

- Ensure you're connected to Adobe VPN
- Check network connectivity
- Verify git access:
  ```bash
  git ls-remote https://git.corp.adobe.com/AdobeDocs/CursorAgents
  ```

## How It Works

Cursor Agents are distributed as a **git submodule**:

```
your-repo/
  ├── .cursor-agents/          ← Git submodule
  │   ├── agents/
  │   │   ├── draft-page-generator.md
  │   │   └── fix-grammar.md
  │   └── AGENTS.md
  ├── setup-agents.sh          ← Setup script
  └── your-content/
```

The submodule points to:
**https://git.corp.adobe.com/AdobeDocs/CursorAgents**

This ensures everyone uses the same, up-to-date agents.

## For Maintainers

### Adding to a new repository

1. Add the submodule:
   ```bash
   git submodule add https://git.corp.adobe.com/AdobeDocs/CursorAgents.git .cursor-agents
   ```

2. Copy setup files:
   - `setup-agents.sh`
   - `setup-agent.md` (place in root, not in submodule)
   - `INSTALL.md`

3. Commit:
   ```bash
   git add .gitmodules .cursor-agents setup-agents.sh
   git commit -m "Add Cursor Agents submodule"
   ```

### Updating the central repository

Changes to agents should be made in:
**https://git.corp.adobe.com/AdobeDocs/CursorAgents**

All repositories will receive updates via `git submodule update --remote`.

---

**Need help?** Contact your documentation team lead or check the internal wiki.
