import discord
from discord.ext import commands

from commands.help import help_page
from commands.patch_notes import patch_notes_page
from commands.format import format_text

bot = commands.Bot(command_prefix='.', description='Bot that adds spaces to your message for emphasizing unnecessary shit')

# On login
@bot.event
async def on_ready(): 
    print('Logged in as')
    print(bot.user.name)
    print('----------------')

commands = ["info", "help", "patch_notes"]


@bot.event
async def on_message(original_message):
    data = original_message.content.split()

    if not data or (data[0][0]!="." and data[0]!=".m"): 
        print("lol")
        return
    
    print("Data:", data)
    if data[0] == ".m": 
        data.pop(0)
        await bot.delete_message(original_message)
        await bot.send_message(original_message.channel, format_text(bot, original_message, data))

    elif data[0] == '.info': 
        embed = discord.Embed(title="Author", description="Kaisu", color=0xeee657)
        await bot.send_message(original_message.channel, embed=embed)

    elif data[0] == ".help": 
        await bot.send_message(original_message.channel, embed=help_page())   

    elif data[0] == ".patch": 
        await bot.send_message(original_message.channel, embed=patch_notes_page())   

    else: 
        print("Do nothing")
        return


bot.run('_YOUR_TOKEN_HERE_')      #Run your token


