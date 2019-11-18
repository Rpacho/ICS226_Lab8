import asyncio

PORT = 12345
# HOST = '::'


async def client():
    AgentList = open("agent.conf", "r")
    AgentHost = AgentList.readline()
    inputCommand = input("What command do you want to be send (type: disk, memory, users): ")
    # HOST = AgentHost.rstrip('\n')
    # reader, writer = await asyncio.open_connection('2620:7800:c000:2259:a9db:3f96:91c3:50e1', PORT)
    # print("Connected to the IP")
    # writer.write(inputCommand.encode('utf-8') + b'\n')
    # await writer.drain()
    while (AgentHost != ""):
        try:
            HOST = AgentHost.rstrip('\n')
            reader, writer = await asyncio.open_connection(HOST, PORT)
            print("Connected to the IP", HOST, '\n')
            writer.write(inputCommand.encode('utf-8') + b'\n')
            await writer.drain()

            output = await reader.read()
            print(output.decode('utf-8'))

            AgentHost = AgentList.readline()
        except:
            print("Can't connect to one of the Agents.")
            # writer.close()
            # await writer.wait_close()
            break


asyncio.run(client())
