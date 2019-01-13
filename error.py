from enum import Enum

class Error(Enum):
    CMD_INVAL = "I'm not sure what you mean by that"
    ARG_INVAL = "That parameter doesn't match the format I need"
    NOT_SERVER = "You need to be in a server to use that command"
    ACCESS_DENIED = "I'm sorry {user}, I'm afraid I can't do that"
    ROLE_NOT_FOUND = "Sorry, I can't find that role"
    BORKED = "Something went wrong, but I don't know what!"

def format_error(msg, err):
    return err.value.format(user=msg.author.mention)
