import asyncio
import datetime
from datetime import date

import discord
from discord import app_commands
from discord.ext import commands

from fun import *

time_order = date.today()
class orders_command(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

        @bot.tree.command(name="приказ", description="выдать приказ игроку")
        @app_commands.describe(member = "Игрок")
        @app_commands.describe(description = "Описание приказа")
        @app_commands.describe(deadline = "Дедлайн")

        async def order(inter: discord.Integration,  member: discord.Member, description : str, deadline : str):
            if(member.display_name.find(' ') > 0):
                await inter.response.send_message(f"Ник - {member.display_name} является некорректным", ephemeral=True)
            else:
                embed = discord.Embed(color=0x2F4F4F)
                embed.add_field(name="Ник", value=f"``` {member.display_name} ```", inline=False)
                embed.add_field(name="Опиание приказа", value=f"``` {description} ```", inline=False)
                embed.add_field(name="Дедлайн", value=f"``` {deadline} ```", inline=False)
                embed.add_field(name="ID", value=f"``` {lowid()} ```", inline=False)
                embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=64&amp;ch=0")
                embed.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                embed.set_footer(text= time_order)

                channel = bot.get_channel(get_channel(1))
                await channel.send(member.mention, embed=embed)

                id_player = member.id
                status = "Не выполнено"
                insert(str(id_player), member.display_name, description, deadline, time_order, str(status))

        @bot.tree.command(name="выполнено", description="подтвердить выполнение приказа")
        @app_commands.describe(id = "ID приказа")
        async def order_complete(inter: discord.Integration, id: int):
            channel = bot.get_channel(get_channel(1))
            newstatus = "Выполнено"
            member = find(id)
            if(member != None):
                status = get_status(id)
                if(status == "Не выполнено"):
                    update(id, str(newstatus))
                    em = discord.Embed(color=0x228B22)
                    em.add_field(name="ID", value=f"``` {id} ```", inline=False)
                    em.add_field(name="Cатус", value=f"``` Выполнено ```", inline=False)
                    em.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                    await channel.send(f"<@{member}>", embed=em)
                else:
                    await inter.response.send_message(f"Данный приказ был - {status}", ephemeral=True)
            else:
               await inter.response.send_message("Приказа с таким Id не существует!", ephemeral=True)

        @bot.tree.command(name="отменить_приказ", description="отменить приказ")
        @app_commands.describe(id = "ID приказа")
        async def order_delete(inter: discord.Integration, id: int):
            channel = bot.get_channel(get_channel(1))
            newstatus = "Отменён"
            member = find(id)
            if(member != None):
                status = get_status(id)
                if(status == "Не выполнено"):
                    update(id, str(newstatus))
                    em = discord.Embed(color=0x8B0000)
                    em.add_field(name="ID", value=f"``` {id} ```", inline=False)
                    em.add_field(name="Cатус", value=f"``` Отменено ```", inline=False)
                    em.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                    await channel.send(f"<@{member}>", embed=em)
                else:
                    await inter.response.send_message(f"Данный приказ был - {status}", ephemeral=True)
            else:
               await inter.response.send_message("Приказа с таким Id не существует!", ephemeral=True)

        @bot.tree.command(name="информация_о_приказе", description="проверить задание, получив его статус и описание")
        @app_commands.describe(id = "ID приказа")
        async def status(inter: discord.Integration, id: int):
            status = get_status(id)
            name = get_name(id)
            description = get_description(id)
            if(status != None and name != None and description != None):
                await inter.response.send_message(f"Информация о приказе под id : **{id}**. Ник: **{name}**, Описание: *{description}*, Статус : **{status}**", ephemeral=True)
            else:
                await inter.response.send_message("Приказа с таким Id не существует!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(orders_command)