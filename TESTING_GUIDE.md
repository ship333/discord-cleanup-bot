# Discord Bot Testing Guide

## Current Issue
❌ **Privileged Intents Required** - The bot needs special permissions enabled in Discord Developer Portal.

## Step-by-Step Setup

### 1. Enable Privileged Intents in Discord Developer Portal
1. Go to https://discord.com/developers/applications/
2. Select your bot application
3. Click **Bot** in the left sidebar
4. Scroll down to **Privileged Gateway Intents**
5. Enable these toggles:
   - ✅ **MESSAGE CONTENT INTENT** (required to read message content)
   - ✅ **SERVER MEMBERS INTENT** (optional but recommended)
   - ✅ **PRESENCE INTENT** (optional)
6. Click **Save Changes**

### 2. Verify Bot Permissions
Make sure your bot has these permissions in the Discord server:
- ✅ Read Messages/View Channels
- ✅ Read Message History
- ✅ Manage Messages (to delete messages)

### 3. Bot Configuration
Current settings in `discord_cleanup.py`:
- **Target User ID:** `1021871981584466002`
- **Target Channel ID:** `1441535358469931060`
- **Delete Delay:** 1.5 seconds

### 4. Test the Bot

#### Option A: Dry Run Test (Recommended First)
Before deleting, let's add a test mode to see what would be deleted:

```python
# Add this flag at the top
DRY_RUN = True  # Set to False to actually delete
```

#### Option B: Run the Bot
```bash
python discord_cleanup.py
```

### 5. Expected Output

#### Successful Login:
```
Logged in as YourBotName#1234
Checking channel: channel-name (1441535358469931060)
```

#### Finding Messages:
```
Deleted: This is a message that was deleted
Deleted: Another message content here
```

#### Completion:
```
✔ Cleanup complete. Exiting.
```

### 6. Troubleshooting

| Error | Solution |
|-------|----------|
| `PrivilegedIntentsRequired` | Enable MESSAGE CONTENT INTENT in Developer Portal |
| `Forbidden` | Bot lacks "Manage Messages" permission in the channel |
| `Channel not found` | Verify channel ID and bot has access to that channel |
| `Unauthorized` | Check if bot token is valid |

### 7. Safety Checks
- ✅ Verify `TARGET_USER_ID` is correct (only this user's messages will be deleted)
- ✅ Verify `TARGET_CHANNEL_IDS` list is correct
- ✅ Test in a test channel first before production
- ✅ Consider backing up important messages

### 8. Rate Limiting
- Current delay: **1.5 seconds** between deletions
- Discord rate limit: ~5 deletions per second
- If you hit rate limits, increase `DELETE_DELAY` to 2-3 seconds

## Quick Test Checklist
- [ ] Privileged intents enabled in Developer Portal
- [ ] Bot has "Manage Messages" permission
- [ ] Bot is in the target server
- [ ] Bot can see the target channel
- [ ] Target user ID is correct
- [ ] Target channel ID is correct
- [ ] Token is valid and not expired
