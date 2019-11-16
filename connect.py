import subprocess
import sys

x = input("Enter the command key!")

f = open("commands.conf", 'r')
data = ""
while(True):
    command = f.readline()

    if x in command:
        data1 = command.rstrip('\n')
        data = data1.split('\t')
        break
    if(command == ""):
        break

#print(data1)
#print(len(data))
if len(data) > 3:
    print(subprocess.check_output([data[1], data[2], data[3]]))
else:
    print(subprocess.check_output([data[1], data[2]]))







#subprocess.check_output(['ls', '/'], encoding='utf-8')
