# Discord Cleanup Bot - Quick Start Guide

## Easy Time Configuration

The script now has a simple configuration section at the top. Just uncomment the option you want to use!

## Common Use Cases

### 1. Delete Last 30 Minutes of Messages
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(minutes=30)
DELETE_BEFORE = None
```

### 2. Delete Last 2 Hours of Messages
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(hours=2)
DELETE_BEFORE = None
```

### 3. Delete Last 7 Days of Messages
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)
DELETE_BEFORE = None
```

### 4. Delete Everything EXCEPT Last 10 Minutes
```python
DELETE_AFTER = None
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(minutes=10)
```

### 5. Delete Messages Between 60 and 30 Minutes Ago
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(minutes=60)
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(minutes=30)
```

### 6. Delete Messages on a Specific Date
```python
# Delete all messages on November 21, 2024
DELETE_AFTER = datetime(2024, 11, 21, 0, 0, tzinfo=timezone.utc)    # Start: Nov 21 midnight
DELETE_BEFORE = datetime(2024, 11, 21, 23, 59, tzinfo=timezone.utc) # End: Nov 21 11:59 PM
```

### 7. Delete Messages From Specific Date Forward
```python
# Delete everything from Nov 15, 2024 onwards
DELETE_AFTER = datetime(2024, 11, 15, 0, 0, tzinfo=timezone.utc)
DELETE_BEFORE = None
```

### 8. Delete Messages Up Until Specific Date
```python
# Delete everything up until Nov 20, 2024
DELETE_AFTER = None
DELETE_BEFORE = datetime(2024, 11, 20, 23, 59, tzinfo=timezone.utc)
```

### 9. Delete ALL Messages (No Time Filter)
```python
DELETE_AFTER = None
DELETE_BEFORE = None
```

## Date/Time Format Reference

### Specific Date/Time Format
```python
datetime(YEAR, MONTH, DAY, HOUR, MINUTE, tzinfo=timezone.utc)
```

**Examples:**
- `datetime(2024, 11, 21, 14, 30, tzinfo=timezone.utc)` = Nov 21, 2024 at 2:30 PM
- `datetime(2024, 12, 25, 0, 0, tzinfo=timezone.utc)` = Dec 25, 2024 at midnight
- `datetime(2024, 1, 1, 23, 59, tzinfo=timezone.utc)` = Jan 1, 2024 at 11:59 PM

### Relative Time Format
```python
datetime.now(timezone.utc) - timedelta(UNIT=VALUE)
```

**Units:**
- `minutes=X` - X minutes ago
- `hours=X` - X hours ago
- `days=X` - X days ago
- `weeks=X` - X weeks ago

**Examples:**
- `timedelta(minutes=15)` = 15 minutes
- `timedelta(hours=3)` = 3 hours
- `timedelta(days=1)` = 1 day
- `timedelta(weeks=2)` = 2 weeks

## Step-by-Step Usage

1. **Open** `discord_cleanup.py`

2. **Set your targets** (lines 9-11):
   ```python
   TOKEN = "your_bot_token"
   TARGET_USER_ID = 1234567890  # User ID
   TARGET_CHANNEL_IDS = [9876543210]  # Channel ID(s)
   ```

3. **Choose a time range** (lines 20-61):
   - Find the option you want
   - Remove the `#` at the start of those lines
   - Make sure to comment out (add `#` to) any other time options

4. **Test first** (line 14):
   ```python
   DRY_RUN = True  # Test mode - won't actually delete
   ```

5. **Run the bot**:
   ```bash
   python discord_cleanup.py
   ```

6. **Review the output** - it will show what would be deleted

7. **Run for real** (if output looks good):
   ```python
   DRY_RUN = False  # Actually delete messages
   ```

8. **Run again**:
   ```bash
   python discord_cleanup.py
   ```

## Tips

- Always test with `DRY_RUN = True` first
- Times are in UTC timezone
- You can only have ONE time configuration active at a time
- Comment out (add `#`) to any options you're not using
- The bot will show timestamps in the output so you can verify
