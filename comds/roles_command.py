from datetime import date

import discord
from discord import app_commands
from discord.ext import commands

from config import max_roles_index
from fun import *

time_order = date.today()
class roles_command(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

        @bot.tree.command(name="принять", description="принять человека в наши ряды")
        @app_commands.describe(member = "Пользователь")
        async def invite_player(inter: discord.Integration, member: discord.Member):
            def roles(role):
                return discord.utils.get( member.guild.roles, id = role)
            try:
                await member.add_roles(roles(get_roles_index(0)))
                await member.add_roles(roles(get_roles_index(1)))
                await inter.response.send_message(f"{member.mention} был принят в армию!", ephemeral=True)
            except Exception:
                await inter.response.send_message("Этот человек уже состоит в армии!", ephemeral=True)

        @bot.tree.command(name="уволить", description="уволить человека из наших рядов")
        @app_commands.describe(member = "Пользователь")
        async def remove_player(inter: discord.Integration, member: discord.Member):
            def roles(role):
                return discord.utils.get( member.guild.roles, id = role)
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)
            try:
                try:
                    await member.remove_roles(roles(get_roles_of_index(0)))
                    await member.remove_roles(roles(get_roles_of_index(1)))
                    await member.remove_roles(roles(get_roles_of_index(2)))
                except Exception:
                    print("#")
                await member.remove_roles(roles(get_roles_index(0)))
                await member.remove_roles(roles(user_role))
                await inter.response.send_message(f"{member.mention} был уволен с армии!", ephemeral=True)
            except Exception:
                await inter.response.send_message("Этот человек не состоит в армии!", ephemeral=True)
        
        @bot.tree.command(name="повысить", description="повысить человека")
        @app_commands.describe(member = "Пользователь")
        async def up_player(inter: discord.Integration, member: discord.Member):
            channel = bot.get_channel(get_channel(0))
            def roles(role):
                return discord.utils.get( member.guild.roles, id = role)
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)
            if(user_role != None and user_role != get_roles_index(max_roles_index)):
                await member.add_roles(roles(find_roles(user_role, 'next')))
                await member.remove_roles(roles(user_role))
                index_role = get_index_user_id_role(user_role)
                if(index_role > 2 and index_role < 8):
                    await member.add_roles(roles(get_roles_of_index(0)))
                elif(index_role >= 8 and index_role < 13):
                    await member.remove_roles(roles(get_roles_of_index(0)))
                    await member.add_roles(roles(get_roles_of_index(1)))
                elif(index_role >= 13):
                    await member.remove_roles(roles(get_roles_of_index(1)))
                    await member.add_roles(roles(get_roles_of_index(2)))
                embed = discord.Embed(color=0x228B22)
                embed.add_field(name='',value=f"{member.mention} был **повышен** до <@&{find_roles(user_role, 'next')}>!")
                embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=48&amp;ch=0")
                embed.set_footer(text= time_order)

                await channel.send(member.mention ,embed = embed)

                await inter.response.send_message(f"{member.mention} был повышен до <@&{find_roles(user_role, 'next')}>!", ephemeral=True)
            else:
                await inter.response.send_message("Больше уже некуда!", ephemeral=True)
            
        @bot.tree.command(name="понизить", description="понизить человека")
        @app_commands.describe(member = "Пользователь")
        async def down_player(inter: discord.Integration, member: discord.Member):
            channel = bot.get_channel(get_channel(0))
            def roles(role):
                return discord.utils.get( member.guild.roles, id = role)
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)
            if(user_role != None and user_role != get_roles_index(1)):
                await member.add_roles(roles(find_roles(user_role, 'prew')))
                await member.remove_roles(roles(user_role))

                index_role = get_index_user_id_role(find_roles(user_role, 'prew'))
                print(index_role)
                if(index_role <= 3 and index_role >= 2):
                    await member.remove_roles(roles(get_roles_of_index(0)))
                elif(index_role <= 8 and index_role >= 4):
                    await member.remove_roles(roles(get_roles_of_index(1)))
                    await member.add_roles(roles(get_roles_of_index(0)))
                elif(index_role <= 13 and index_role >= 9):
                    await member.remove_roles(roles(get_roles_of_index(2)))
                    await member.add_roles(roles(get_roles_of_index(1)))
                embed = discord.Embed(color=0x8B0000)
                embed.add_field(name='',value=f"{member.mention} был **понижен** до <@&{find_roles(user_role, 'prew')}> !")
                embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=48&amp;ch=0")
                embed.set_footer(text= time_order)
                await channel.send(member.mention ,embed = embed)

                await inter.response.send_message(f"{member.mention} был понижен до <@&{find_roles(user_role, 'prew')}>!", ephemeral=True)
            else:
                await inter.response.send_message("Больше уже некуда!", ephemeral=True)


            
                        



async def setup(bot):
    await bot.add_cog(roles_command)