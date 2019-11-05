
import discord
from discord.ext import commands

def format_text(bot, original_message, data): 
    #  if data[0] == ".": 
    #      data.pop(0)
    #  else: 
    #      data[0] = data[0][1:]
    new_message = ""
    for word in data: 
        for character in word: 
            if character == "~":
                new_message += character
            else: 
                new_message += character + " "
        new_message += " "
    print(new_message)
    #  new_message = original_message.author.name + ": "+ new_message
    new_message = "***" + new_message + "***"
    return new_message

    #  try: 
    #  except(discord.errors.NotFound): 
    #      print("Exception raised")
        #  await bot.send_message(original_message.channel, "Please notify the stupid programmer that there is something wrong w/ his bloody code")

