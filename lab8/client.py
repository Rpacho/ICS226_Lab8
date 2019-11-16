import asyncio

PORT = 12345


async def runCommand(reader, writer):
    writer.write("hello".encode('utf-8'))
    await writer.drain()
    writer.close()
    await writer.wait_closed()



async def main():
    server = await asyncio.start_server(runCommand, '::', PORT)
    await server.serve_forever()

asyncio.run(main())


