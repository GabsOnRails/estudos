# exercício para administrar o sistema atraves do "subprocess", achei interessante pois o subprocess funciona através de comandos shell
# ,ou seja, funciona perfeitamente no linux.
import subprocess

subprocess.run(['ls','-l','cifradecesar.py'])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# funciona assim também
# subprocess.run(["uname","-a"])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])