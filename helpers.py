def find_role(server, role_name):
    for role in server.roles:
        if role.name == role_name:
            return role

async def delete_messages(client, *msgs):
    if len(msgs) == 0:
        pass
    elif len(msgs) == 1:
        await client.delete_message(msgs[0])
    else:
        await client.delete_messages(msgs)
