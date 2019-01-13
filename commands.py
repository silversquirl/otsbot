import config
from error import Error
from permissions import *
from decorators import *
from helpers import *

@command
async def iam(client, msg, role_name):
    role_name = role_name.strip()
    if role_name.startswith(config.admin_prefix):
        return Error.ACCESS_DENIED
    for role in msg.server.roles:
        if role_name.lower() == role.name.lower():
            await client.add_roles(msg.author, role)
            return "Role {} given to {}".format(role.name, msg.author.mention)
    return Error.ROLE_NOT_FOUND

@command(purge=False, channel_locked=False)
@permission(DiscordPerm.MANAGE_MESSAGES)
async def clean(client, msg, num_s):
    if not num_s.isnumeric():
        return await error(msg, Error.ARG_INVAL)

    await client.delete_message(msg)

    num = int(num_s)
    log = []
    async for entry in client.logs_from(msg.channel, limit=num):
        log.append(entry)
    await delete_messages(client, *log)
