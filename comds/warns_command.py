from datetime import date

import discord
import pymysql
from discord import app_commands
from discord.ext import commands

from fun import *

time_warn = date.today()
class warns_command(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

        @bot.tree.command(name="выдать_выговор", description="выдать выговор")
        async def add_warn_player(inter : discord.Integration, member : discord.Member, description : str):
            def roles(role):
                return discord.utils.get( member.guild.roles, id = role)
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)

            if(user_role != None):

                if(get_warns_player(member.display_name) < 2):
                    channel = bot.get_channel(get_channel(2))
                    add_warn(member.display_name, member.id)
                    info = get_warns_player(member.display_name)
                    embed = discord.Embed(color=0x8B0000)
                    embed.add_field(name='',value=f"{member.mention} был выдан выговор ({info})", inline=False)
                    embed.add_field(name='Причина:',value=f"{description}", inline=False)
                    embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=48&amp;ch=0")
                    embed.set_footer(text= time_warn)
                    embed.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                    await channel.send(member.mention, embed=embed)

                else:
                    try:
                        await member.remove_roles(roles(get_roles_of_index(0)))
                        await member.remove_roles(roles(get_roles_of_index(1)))
                        await member.remove_roles(roles(get_roles_of_index(2)))
                    except Exception:
                        print("#")
                    await member.remove_roles(roles(get_roles_index(0)))
                    await member.remove_roles(roles(user_role))
                    remove_warns(member.display_name)
                    embed = discord.Embed(color=0x8B0000)
                    embed.add_field(name='',value=f"{member.mention} был выдан выговор (3)", inline=False)
                    embed.add_field(name='Причина:',value=f"{description}", inline=False)
                    embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=48&amp;ch=0")
                    embed.set_footer(text= time_warn)
                    embed.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                    await channel.send(member.mention, embed=embed)
                    await inter.response.send_message(f"{member.mention} был уволен с армии из-за 3/3 выговоров!", ephemeral=True)
            else:
                await inter.response.send_message("Этот человек не состоит в армии!", ephemeral=True)
                    
        @bot.tree.command(name="убрать_выговор", description="убрать выговор")
        async def remove_warn_player(inter : discord.Integration, member : discord.Member, description : str):
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)
            if(user_role != None):
                if(get_warns_player(member.display_name) > 0):
                    channel = bot.get_channel(get_channel(2))
                    remove_warn(member.display_name)
                    info = get_warns_player(member.display_name)
                    embed = discord.Embed(color=0x228B22)
                    embed.add_field(name='',value=f"{member.mention} был убран выговор ({info})", inline=False)
                    embed.set_thumbnail(url=f"https://plasmorp.com/avatar/{member.display_name}?w=48&amp;ch=0")
                    embed.add_field(name='Причина:',value=f"{description}", inline=False)
                    embed.set_footer(text= time_warn)
                    embed.set_author(name= inter.user.display_name, icon_url= inter.user.avatar)
                    await channel.send(member.mention, embed=embed)
                else:
                    await inter.response.send_message(f"У солдата {member.mention} - {info} выговоров", ephemeral=True)
            else:
                await inter.response.send_message("Этот человек не состоит в армии!", ephemeral=True)
        @bot.tree.command(name="информация_о_выговоре", description="получить информацию о выговорах")
        async def info_warn_player(inter : discord.Integration, member : discord.Member):
            name_ = []
            name = member.roles
            for i in name:
                name_.append(str(i))
            user_role = find_id_roles_namelist(name_)

            if(user_role != None):
                info = get_warns_player(member.display_name)
                await inter.response.send_message(f"У солдата {member.mention} - {info} выговоров", ephemeral=True)
            else:
                await inter.response.send_message("Этот человек не состоит в армии!", ephemeral=True)



async def setup(bot):
    await bot.add_cog(warns_command)