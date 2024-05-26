import discord
import requests

client = discord.Client()

# Function to request guild ID, channel ID, and webhook URL
async def request_guild_channel_and_webhook():
    print("Please enter the Guild ID:")
    guild_id = input()
    print("Please enter the Channel ID:")
    channel_id = input()
    print("Please enter the Webhook URL:")
    webhook_url = input()
    return int(guild_id), int(channel_id), webhook_url

# Replace 'YOUR_BOT_TOKEN' with your own bot token
bot_token = 'YOUR_BOT_TOKEN'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    guild_id, channel_id, webhook_url = await request_guild_channel_and_webhook()
    print(f'Starting message scraping for Guild ID: {guild_id}, Channel ID: {channel_id}')
    await scrape_messages(guild_id, channel_id, webhook_url)

async def scrape_messages(guild_id, channel_id, webhook_url):
    guild = client.get_guild(guild_id)
    channel = guild.get_channel(channel_id)
    async for message in channel.history(limit=None):
        # Construct the message to send to the webhook
        payload = {
            'content': f'Message from {message.author.name} at {message.created_at}: {message.content}'
        }
        # Send the message to the webhook
        requests.post(webhook_url, json=payload)
    print("Scraping completed. Press any key to exit.")
    input()  # Pauses the script until any key is pressed

# Run the bot with the bot token
client.run(bot_token)