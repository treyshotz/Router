import requests
from requests.auth import HTTPBasicAuth

checkip = requests.get("http://192.168.1.102")
print(checkip)