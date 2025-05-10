import os
import discord
from discord.ext import commands, tasks
import sqlite3
import requests
from bs4 import BeautifulSoup

# Get environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# Discord bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
def init_db():
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS games (name TEXT, url TEXT, price TEXT)''')
    conn.commit()
    conn.close()

def add_game(game_name, url):
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute("INSERT INTO games (name, url, price) VALUES (?, ?, ?)", (game_name, url, "Not Checked"))
    conn.commit()
    conn.close()

def remove_game(game_name):
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute("DELETE FROM games WHERE name=?", (game_name,))
    conn.commit()
    conn.close()

def get_games():
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    games = c.execute("SELECT name, url, price FROM games").fetchall()
    conn.close()
    return games

# Price Scraping
def get_steam_price(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_container = soup.find('div', class_='game_purchase_price')
    return price_container.text.strip() if price_container else "Price not found"

def get_cdkeys_price(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_container = soup.find('span', class_='price')
    return price_container.text.strip() if price_container else "Price not found"

# Bot commands
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_prices.start()  # Start price checking loop

@bot.command()
async def addgame(ctx, game_name: str, url: str):
    add_game(game_name, url)
    await ctx.send(f'✅ Added **{game_name}** to tracking list!')

@bot.command()
async def removegame(ctx, game_name: str):
    remove_game(game_name)
    await ctx.send(f'❌ Removed **{game_name}** from tracking list.')

@tasks.loop(hours=1)
async def check_prices():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)  # Replace with your channel ID
    games = get_games()
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    
    for name, url, old_price in games:
        new_price = get_steam_price(url) if "store.steampowered.com" in url else get_cdkeys_price(url)

        if new_price != old_price:
            await channel.send(f'🔔 **Price Change:** {name} is now **{new_price}**!\n🔗 {url}')
            c.execute("UPDATE games SET price=? WHERE name=?", (new_price, name))
            conn.commit()
    
    conn.close()

# Run bot
init_db()
bot.run(DISCORD_TOKEN)
