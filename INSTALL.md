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

3. Follow the prompts
4. Done! ✨

### Option 2: Using Terminal

1. Open your terminal in the repository root
2. Run:

   ```bash
   ./setup-agents.sh
   ```

   Or manually:

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

See `.cursor-agents/AGENTS.md` for full list of available agents.

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
journey-optimizer.en/
  ├── .cursor-agents/          ← Git submodule
  │   ├── agents/
  │   │   ├── draft-page-generator.md
  │   │   └── fix-grammar.md
  │   └── AGENTS.md
  ├── setup-agents.sh          ← Setup script
  ├── setup-agent.md           ← Bootstrap agent
  └── help/                    ← Your documentation
```

The submodule points to:
**https://git.corp.adobe.com/AdobeDocs/CursorAgents**

This ensures everyone uses the same, up-to-date agents.

**Need help?** Contact your documentation team lead or check the internal wiki.

