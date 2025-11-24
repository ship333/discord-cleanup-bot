"""
Quick test script to verify bot can connect and see the channel
"""
import discord

TOKEN = "MTQ0MTUzNTY0MDg1OTgzNjYwOA.GOfbT0.WlOeQiUPv5wxAGDyRUfD2PlsFhn7v2b2dZo1B8"
TARGET_CHANNEL_ID = 1441535358469931060

class TestBot(discord.Client):
    async def on_ready(self):
        print(f"✅ Successfully logged in as {self.user}")
        print(f"Bot ID: {self.user.id}")
        print(f"\nGuilds (Servers) the bot is in:")
        
        for guild in self.guilds:
            print(f"  - {guild.name} (ID: {guild.id})")
        
        print(f"\nLooking for channel {TARGET_CHANNEL_ID}...")
        channel = self.get_channel(TARGET_CHANNEL_ID)
        
        if channel:
            print(f"✅ Found channel: {channel.name}")
            print(f"   Type: {channel.type}")
            print(f"   Guild: {channel.guild.name}")
            
            # Check permissions
            permissions = channel.permissions_for(channel.guild.me)
            print(f"\nBot permissions in this channel:")
            print(f"  - Read Messages: {permissions.read_messages}")
            print(f"  - Read Message History: {permissions.read_message_history}")
            print(f"  - Manage Messages: {permissions.manage_messages}")
            
            if not permissions.manage_messages:
                print("\n⚠️  WARNING: Bot lacks 'Manage Messages' permission!")
                print("   The bot won't be able to delete messages.")
        else:
            print(f"❌ Channel not found!")
            print("   Possible reasons:")
            print("   - Bot doesn't have access to this channel")
            print("   - Channel ID is incorrect")
            print("   - Bot is not in the server containing this channel")
        
        print("\n✔ Connection test complete. Closing...")
        await self.close()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = TestBot(intents=intents)
client.run(TOKEN)
