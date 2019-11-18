#!/usr/bin/python3

import asyncio

PORT = 12345
# HOST = '::'


async def client():
    AgentList = open("agent.conf", "r")
    AgentHost = AgentList.readline()
    inputCommand = input("What command do you want to be send (type: disk, memory, users): ")
    while (AgentHost != ""):
        try:
            HOST = AgentHost.rstrip('\n')
            reader, writer = await asyncio.open_connection(HOST, PORT)

            print("IP: ", HOST)
            writer.write(inputCommand.encode('utf-8') + b'\n')
            await writer.drain()

            output = await reader.read()
            print(output.decode('utf-8'))

            AgentHost = AgentList.readline()
            writer.close()
            await writer.wait_closed()
        except:
            print("Can't connect to one of the Agents.")
            writer.close()
            await writer.wait_closed()
            break


asyncio.run(client())
