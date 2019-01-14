import discord
import asyncio
import config
import decorators
import commands
from error import Error

client = discord.Client()

@decorators.command
async def invalid_commandD(client, msg, role_name):
    return Error.CMD_INVAL

@client.event
async def on_ready():
    print("Logged in as", client.user.name)

@client.event
async def on_message(msg):
    if msg.content.startswith('^'):
        cmd, arg = msg.content[1:].split(' ', 1)
        command_fun = decorators.commands.get(cmd.lower(), invalid_commandD)
        await command_fun(client, msg, arg)

# TODO: hook role creation and deletion to update roles message
# TODO: create roles message if it doesn't exist

client.run(config.access_tok)
