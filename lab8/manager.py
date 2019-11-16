import asyncio

PORT = 12345
HOST = '::'


async def client():
    while (True):
        reader, writer = await asyncio.open_connection(HOST, PORT)
        inputCommand = input("What command do you want to be send (type: disk, memory, users): ")
        writer.write(inputCommand.encode('utf-8') + b'\n')
        await writer.drain()

        output = await reader.read()
        print(output.decode('utf-8'))
    # writer.close()
    # await writer.wait_close()

asyncio.run(client())
