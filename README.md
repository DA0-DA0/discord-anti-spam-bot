# DAO DAO Anti-Spam Discord Bot

This is a Discord bot that automatically detects spammers, deletes their
messages, notifies an admin channel, and times out the user for 27 days.

## Set up

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

```bash
cp .env.example .env
```

Set the following environment variables in the `.env` file:

- `TOKEN`: The Discord bot token.
- `GUILD_ID`: The Discord guild ID.
- `NOTIFY_CHANNEL_ID`: The Discord channel ID to notify when a spammer is
  detected.

### Run the bot

```bash
python bot.py
```

## Docker

### Building the bot

```bash
docker build -t daodao-discord-anti-spam-bot .
```

### Running the bot

```bash
docker run --rm --name discord-bot \
  -e TOKEN="your_discord_token" \
  -e GUILD_ID="your_guild_id" \
  -e NOTIFY_CHANNEL_ID="your_notify_channel_id" \
  daodao-discord-anti-spam-bot
```
