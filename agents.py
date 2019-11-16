
import asyncio
import subprocess

PORT = 12345

agent = "agent.conf"


async def runCommand(reader, writer):
    # writer.write("hello".encode('utf-8'))
    # await writer.drain()
    # writer.close()
    # await writer.wait_closed()
    command = await reader.readline()

    comDecode = command.decode('utf-8')
    dataRecieve = comDecode.rstrip('\n')
    f = open("commands.conf", 'r')
    array = []

    while(True):
        exucuteCommand = f.readline()
        # print(command)
        # if "disk" == command:
            # print(True)
        # print("in while")
        dataStripNewLine = exucuteCommand.rstrip('\n')
        if dataRecieve in exucuteCommand:
            data = dataStripNewLine.split('\t')
            # for i in range (len(data)):
            #     array.append(data[i])
            break
        if(exucuteCommand == ""):
            # print("empty")
            break
    if len(data) > 3:
        dataToSend = subprocess.check_output([data[1], data[2], data[3]])
    else:
        dataToSend = subprocess.check_output([data[1], data[2]])

    writer.write(dataToSend)
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(runCommand, '::', PORT)
    await server.serve_forever()

asyncio.run(main())




