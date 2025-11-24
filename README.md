# Discord Message Cleanup Bot

A bot to delete messages from a specific user in specified Discord channels.

## Files

- **`discord_cleanup.py`** - Main bot script with DRY_RUN mode
- **`test_bot_connection.py`** - Test script to verify bot setup
- **`TESTING_GUIDE.md`** - Detailed testing and troubleshooting guide

## Quick Start

### Step 1: Enable Privileged Intents (REQUIRED)

1. Go to <https://discord.com/developers/applications/>
2. Select your bot application
3. Click **Bot** → Scroll to **Privileged Gateway Intents**
4. Enable **MESSAGE CONTENT INTENT**
5. Click **Save Changes**

### Step 2: Test Bot Connection

```bash
python test_bot_connection.py
```

This will verify:
- ✅ Bot can log in
- ✅ Bot can see the target channel
- ✅ Bot has correct permissions

### Step 3: Run in Dry-Run Mode (Safe Test)

```bash
python discord_cleanup.py
```

The bot is currently in **DRY_RUN mode** (line 9). It will show what would be deleted without actually deleting anything.

### Step 4: Run for Real

1. Open `discord_cleanup.py`
2. Change line 9: `DRY_RUN = False`
3. Run: `python discord_cleanup.py`

## Configuration

Edit these values in `discord_cleanup.py`:

```python
TARGET_USER_ID = 1021871981584466002  # User whose messages to delete
TARGET_CHANNEL_IDS = [1441535358469931060]  # Channels to scan
DELETE_DELAY = 1.5  # Seconds between deletions
DRY_RUN = True  # Set to False to actually delete

# Time filters (optional)
DELETE_AFTER = None  # Delete messages after this date
DELETE_BEFORE = None  # Delete messages before this date
```

### Time-Based Filtering

Delete messages within specific date ranges. See `TIME_FILTER_GUIDE.md` for detailed examples.

**Quick examples:**

```python
# Last 7 days only
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)

# Older than 30 days
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(days=30)

# Specific date range
DELETE_AFTER = datetime(2024, 11, 1, tzinfo=timezone.utc)
DELETE_BEFORE = datetime(2024, 11, 21, tzinfo=timezone.utc)
```

## Common Issues

| Error | Solution |
|-------|----------|
| `PrivilegedIntentsRequired` | Enable MESSAGE CONTENT INTENT in Developer Portal |
| `Forbidden` | Bot needs "Manage Messages" permission |
| `Channel not found` | Verify channel ID and bot access |

## Safety Features

- ✅ DRY_RUN mode for testing
- ✅ Only deletes from specified user ID
- ✅ Only scans specified channels
- ✅ Rate limiting with configurable delay
- ✅ Detailed logging of all actions

## Output Example

```text
Logged in as YourBot#1234

⚠️  DRY RUN MODE - No messages will be deleted

📝 Checking channel: general (1441535358469931060)
[DRY RUN] Would delete: Test message 1
[DRY RUN] Would delete: Test message 2
Found 2 messages in this channel

==================================================
Total messages found: 2
==================================================

✔ Cleanup complete. Exiting.
```
