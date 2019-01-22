import os 
import subprocess

default = subprocess.check_output(ipconfig, shell=True)
gateway = str(default)
print("Hei starter print")
print(gateway)
f = open("config.txt", "w+")
f.write(gateway)
f.close()