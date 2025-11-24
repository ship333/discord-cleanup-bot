import discord
import asyncio
from datetime import datetime, timezone, timedelta

# ============================================================================
# EASY CONFIGURATION - EDIT THESE VALUES
# ============================================================================

TOKEN = "MTQ0MTUzNTY0MDg1OTgzNjYwOA.GOfbT0.WlOeQiUPv5wxAGDyRUfD2PlsFhn7v2b2dZo1B8"
TARGET_USER_ID = 1021871981584466002  # User whose messages to delete
TARGET_CHANNEL_IDS = [1441535358469931060,1441543844456828949,1441543955232850065]  # Channels to search

# TEST MODE: See what would be deleted without actually deleting
DRY_RUN = False # Set to True for testing, False to actually delete

# ============================================================================
# TIME RANGE CONFIGURATION (Choose ONE option below)
# ============================================================================

# OPTION 1: Delete messages from a RELATIVE time range (recommended)
# Uncomment ONE of these presets:

# Last X minutes:
# DELETE_AFTER = datetime.now(timezone.utc) - timedelta(minutes=30)
# DELETE_BEFORE = None

# Last X hours:
# DELETE_AFTER = datetime.now(timezone.utc) - timedelta(hours=2)
# DELETE_BEFORE = None

# Last X days:
# DELETE_AFTER = datetime.now(timezone.utc) - timedelta(days=7)
# DELETE_BEFORE = None

# Everything EXCEPT last X minutes (delete old, keep recent):
# DELETE_AFTER = None
# DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(minutes=10)

# Time window (e.g., messages between 60 and 30 minutes ago):
# DELETE_AFTER = datetime.now(timezone.utc) - timedelta(minutes=60)
# DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(minutes=30)

# OPTION 2: Delete messages from SPECIFIC dates/times
# Format: datetime(YEAR, MONTH, DAY, HOUR, MINUTE, tzinfo=timezone.utc)
# Use 24-hour format for HOUR (0-23)

# Example: Delete messages from Nov 21, 2024 at 2:00 PM onwards
# DELETE_AFTER = datetime(2024, 11, 21, 14, 0, tzinfo=timezone.utc)
# DELETE_BEFORE = None

# Example: Delete messages up until Nov 21, 2024 at 3:00 PM
# DELETE_AFTER = None
# DELETE_BEFORE = datetime(2024, 11, 21, 15, 0, tzinfo=timezone.utc)

# Example: Delete messages between two specific dates
# DELETE_AFTER = datetime(2024, 11, 1, 0, 0, tzinfo=timezone.utc)   # Nov 1, 2024 midnight
# DELETE_BEFORE = datetime(2024, 11, 21, 23, 59, tzinfo=timezone.utc) # Nov 21, 2024 11:59 PM

# OPTION 3: Delete ALL messages (no time filter)
DELETE_AFTER = None 
DELETE_BEFORE = datetime.now(timezone.utc) - timedelta(minutes=10)
# ============================================================================

# Rate limiting (seconds to wait between deletions)
DELETE_DELAY = 1.5  # Increase if you hit rate limits

class CleanupBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        await self.cleanup_messages()

    async def cleanup_messages(self):
        total_found = 0
        total_deleted = 0
        total_skipped = 0
        
        if DRY_RUN:
            print("\n⚠️  DRY RUN MODE - No messages will be deleted\n")
        
        # Display time filter settings
        if DELETE_AFTER or DELETE_BEFORE:
            print("\n⏰ Time Filter Active:")
            if DELETE_AFTER:
                print(f"   Delete messages AFTER: {DELETE_AFTER.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            if DELETE_BEFORE:
                print(f"   Delete messages BEFORE: {DELETE_BEFORE.strftime('%Y-%m-%d %H:%M:%S %Z')}")
            print()
        
        for channel_id in TARGET_CHANNEL_IDS:
            channel = self.get_channel(channel_id)

            if channel is None:
                print(f"❌ Channel {channel_id} not found!")
                continue

            print(f"\n📝 Checking channel: {channel.name} ({channel.id})")
            channel_count = 0

            async for msg in channel.history(limit=None, oldest_first=True):
                if msg.author.id == TARGET_USER_ID:
                    # Check time filters
                    msg_time = msg.created_at
                    
                    # Skip if message is outside time range
                    if DELETE_AFTER and msg_time < DELETE_AFTER:
                        total_skipped += 1
                        continue
                    
                    if DELETE_BEFORE and msg_time > DELETE_BEFORE:
                        total_skipped += 1
                        continue
                    
                    total_found += 1
                    channel_count += 1
                    
                    try:
                        msg_date_str = msg_time.strftime('%Y-%m-%d %H:%M')
                        if DRY_RUN:
                            print(f"[DRY RUN] Would delete [{msg_date_str}]: {msg.content[:50]}")
                        else:
                            await msg.delete()
                            print(f"✅ Deleted [{msg_date_str}]: {msg.content[:50]}")
                            total_deleted += 1
                        await asyncio.sleep(DELETE_DELAY)
                    except Exception as e:
                        print(f"❌ Failed to delete message: {e}")
            
            print(f"Found {channel_count} messages in this channel")

        print(f"\n{'='*50}")
        if total_skipped > 0:
            print(f"Messages skipped (outside time range): {total_skipped}")
        print(f"Total messages found (in time range): {total_found}")
        if not DRY_RUN:
            print(f"Total messages deleted: {total_deleted}")
        print(f"{'='*50}")
        print("\n✔ Cleanup complete. Exiting.")
        await self.close()

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
intents.guilds = True
intents.messages = True
client = CleanupBot(intents=intents)
client.run(TOKEN)
