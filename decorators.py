import discord
import asyncio
import config
from error import Error, format_error
from permissions import *

commands = {}

def command(fn=None, *, purge=True, channel_locked=True):
    if not fn:
        return lambda fn: command(fn, purge=purge, channel_locked=channel_locked)
    async def _(client, msg, param):
        if not msg.server:
            ret = Error.NOT_SERVER
        else: 
            if channel_locked and msg.channel.name != config.bot_channel:
                return

            try:
                ret = await fn(client, msg, param)
            except discord.Forbidden as e:
                ret = Error.ACCESS_DENIED
            except:
                ret = Error.BORKED

        to_purge = [msg]
        if ret is not None:
            if isinstance(ret, Error):
                ret = format_error(msg, ret)
            else:
                ret = str(ret)
            to_purge.append(await client.send_message(msg.channel, str(ret)))

        if purge:
            await asyncio.sleep(30)
            await client.delete_messages(to_purge)
    _.__name__ = fn.__name__
    commands[fn.__name__] = _
    return _

def permission(*perms):
    def _(fn):
        async def _(client, msg, param):
            user_dcperms = msg.channel.permissions_for(msg.author)
            for perm in perms:
                if isinstance(perm, DiscordPerm):
                    if not getattr(user_dcperms, perm.value):
                        return Error.ACCESS_DENIED
                # TODO: custom permissions
            return await fn(client, msg, param)
        _.__name__ = fn.__name__
        return _
    return _
