# Game Price Tracker Bot 🎮

A Discord bot for tracking game prices on Steam and CDKeys, sending alerts for discounts, price changes, and new releases.

---

## 🚀 Features

- Track game prices from Steam & CDKeys.
- Automated price checks every hour.
- Instant notifications for price drops or new releases.
- Discord commands for adding, removing, and updating tracked games.
- Database storage for game details, price history, and storefront links.

---

## ⚙️ Commands

| Command | Description |
| ----------- | ----------- |
|`/gt_add <name/steam_id>` | Add a game to tracking using its name or Steam ID.|
|`/gt_remove <name/steam_id>` | Remove a tracked game using name or Steam ID. Can also show a list for selection.|
|`/gt_info <name/steam_id>` | Retrieve game details from the database, including publisher, image, and price history.|
|`/gt_list` | Show a full list of all tracked games.|
|`/gt_update <name/steam_id>` | Manually update the price check for a specific game.|
|`/gt_db` | Print the full database table for debugging.|

---

## 🗄️ Database Structure

| Field | Description |
| ----------- | ----------- |
|name | Game title |
|bio | Game description |
|image | Thumbnail or cover art |
|publisher | Game publisher |
|steam_id | Steam game ID |
|steam_link | Steam store page |
|cdkeys_link | CDKeys store page |
|last_price | Previous recorded price |
|current_price | Latest checked price |
|last_checked | Timestamp of the last price check |

---

<!-- ## 🛠 Installation & Setup

1. Clone the Repository

```sh
git clone https://github.com/YOUR_USERNAME/game-price-tracker.git
cd game-price-tracker
```

2. Install Dependencies

```sh
pip install -r requirements.txt
```

3. Set Up Environment Variables Create a .env file or pass variables in Docker:

```
DISCORD_TOKEN=your_bot_token
DISCORD_CHANNEL_ID=your_channel_id
```

4. Run the Bot

```sh
python bot.py
```

## 📦 Docker Setup

1. Build the Docker image

```sh
docker build -t game-price-tracker .
```

2. Run the container

```sh
docker run -d --name tracker-bot \
    -e DISCORD_TOKEN="your_bot_token" \
    -e DISCORD_CHANNEL_ID="your_channel_id" \
    game-price-tracker
``` -->

## 📢 How It Works

- The bot automatically checks for game price changes every hour.
- If a game’s price changes, it sends an alert to your Discord server.
- Users can manually track, remove, and view game details using Discord commands.
- Prices are stored in a database for history and analytics.

---

## 🌟 Future Enhancements

- 🛒 Support more storefronts (Epic, GOG, etc.).
- 📊 Price trend analysis & visual charts.
- 🌍 Regional price tracking.
- 🏷 Wishlist integration with Steam.