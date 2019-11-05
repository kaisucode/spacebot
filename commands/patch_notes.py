
import discord
from discord.ext import commands

def patch_notes_page(): 
    date = "May 2, 2018: \n\n"
    patches = []
    patches.append("- Bot prefix now works like this: \".m your_message\"\n")
    patches.append("- The messages are now italicized and bolded\n")
    patches.append("- Added info, help, and patch notes pages\n")

    description_message = date
    for patch in patches: 
        description_message+=patch

    embed = discord.Embed(title="shadowbot patch notes", description=description_message, color=0xeee657)
    return embed

