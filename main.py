import os

import discord
from discord import app_commands
from discord.ext import commands

from comds.orders_command import orders_command
from comds.roles_command import roles_command
from comds.warns_command import warns_command
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) 


@bot.event
async def on_ready():
    print("Bot is ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

bot.add_cog(orders_command(bot))
bot.add_cog(roles_command(bot))
bot.add_cog(warns_command(bot))
          
bot.run(TOKEN) 