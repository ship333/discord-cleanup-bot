# How to Invite Your Bot to Discord Server

## Step 1: Generate Invite Link

1. Go to <https://discord.com/developers/applications/>
2. Select your bot application
3. Click **OAuth2** in the left sidebar
4. Click **URL Generator**

## Step 2: Select Scopes

Check these boxes:
- ✅ **bot**

## Step 3: Select Bot Permissions

Check these permissions:
- ✅ **Read Messages/View Channels**
- ✅ **Read Message History**
- ✅ **Manage Messages** (required to delete messages)

## Step 4: Copy and Use the Invite Link

1. Scroll down and copy the **Generated URL**
2. Paste it in your browser
3. Select the server you want to add the bot to
4. Click **Authorize**
5. Complete the CAPTCHA if prompted

## Quick Permissions Calculator

Alternatively, use this direct link (replace YOUR_BOT_ID with your bot's ID):

```
https://discord.com/api/oauth2/authorize?client_id=1441535640859836608&permissions=76800&scope=bot
```

Your Bot ID: **1441535640859836608**

Direct invite link:
<https://discord.com/api/oauth2/authorize?client_id=1441535640859836608&permissions=76800&scope=bot>

## After Inviting

Run the test again to verify:

```bash
python test_bot_connection.py
```

You should now see your server listed under "Guilds (Servers) the bot is in".
