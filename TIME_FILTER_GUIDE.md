# Time-Based Message Deletion Guide

The cleanup script now supports filtering messages by date/time ranges.

## Configuration Options

Edit lines 18-26 in `discord_cleanup.py`:

### 1. Delete All Messages (Default)
```python
DELETE_AFTER = None
DELETE_BEFORE = None
```
Deletes all messages from the target user, regardless of date.

### 2. Delete Messages from Last 7 Days
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)
DELETE_BEFORE = None
```

### 3. Delete Messages from Last 30 Days
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=30)
DELETE_BEFORE = None
```

### 4. Delete Only Old Messages (Older than 7 days)
```python
DELETE_AFTER = None
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(days=7)
```

### 5. Delete Messages in Specific Date Range
```python
DELETE_AFTER = datetime(2024, 11, 1, tzinfo=timezone.utc)   # From Nov 1, 2024
DELETE_BEFORE = datetime(2024, 11, 21, tzinfo=timezone.utc)  # Until Nov 21, 2024
```

### 6. Delete Messages from Specific Date Forward
```python
DELETE_AFTER = datetime(2024, 11, 15, tzinfo=timezone.utc)  # From Nov 15, 2024 onwards
DELETE_BEFORE = None
```

### 7. Delete Messages Up to Specific Date
```python
DELETE_AFTER = None
DELETE_BEFORE = datetime(2024, 11, 15, tzinfo=timezone.utc)  # Up to Nov 15, 2024
```

## Time Units Reference

```python
# Hours
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(hours=24)

# Days
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)

# Weeks
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(weeks=2)

# Months (approximate)
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=30)
```

## Example Output

When time filters are active, you'll see:

```
⏰ Time Filter Active:
   Delete messages AFTER: 2024-11-14 13:42:00 UTC

📝 Checking channel: general (1441535358469931060)
✅ Deleted [2024-11-21 13:30]: crack
✅ Deleted [2024-11-21 13:31]: money
Messages skipped (outside time range): 15
Total messages found (in time range): 23
Total messages deleted: 23
```

## Testing Time Filters

**Always test with DRY_RUN first:**

1. Set your time filter (e.g., `DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)`)
2. Set `DRY_RUN = True`
3. Run: `python discord_cleanup.py`
4. Review the output to see which messages would be deleted
5. If correct, set `DRY_RUN = False` and run again

## Common Use Cases

### Delete Today's Messages Only
```python
from datetime import datetime, timezone

# Start of today (UTC)
today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
DELETE_AFTER = today_start
DELETE_BEFORE = None
```

### Delete This Week's Messages
```python
DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)
DELETE_BEFORE = None
```

### Delete Everything Except Last 24 Hours
```python
DELETE_AFTER = None
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(hours=24)
```

## Important Notes

- All times use UTC timezone
- Message timestamps show when the message was created
- Skipped messages (outside time range) are counted but not deleted
- Time filters work with DRY_RUN mode for safe testing
