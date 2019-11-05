import discord
from discord.ext import commands

def help_page(): 
    embed = discord.Embed(title="Shadowbot", description="List of commands are:", color=0xeee657)

    embed.add_field(name=".m [message]", value="Adds spaces, bolds, and italicizes your message", inline=False)
    embed.add_field(name=".info", value="Shows info", inline=False)
    embed.add_field(name=".patch", value="Shows patch notes", inline=False)
    embed.add_field(name=".help", value="Shows help page, but i suppose if you're reading this then you already know", inline=False)
    return embed

