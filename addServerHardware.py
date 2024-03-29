# With this script, physically installed and IP addresses given HPE Hosts can be added to oneview. (Adding Server Hardware) 

#@author Mustafa Yıldırım

from time import sleep
import requests
import json
import urllib3
import time
urllib3.disable_warnings() #With this statement, SSL warnings that is being received everytime the script is run is ignored.

#==========================================Variables that needs to be edited accordingly your environment==========================================================
hostList=['10.83.7.142','10.83.7.140','10.83.7.139','10.83.7.172','10.83.7.170','10.83.7.169']# Hosts iLO ip addresses that is intented to be added to oneview
oneviewip="X.X.X.X" # Oneview IP Address 
auth_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Authenticatin token that is generated by "getAuthToken.py" in this repo or via POST login-sessions API call
#===================================================================================================================================



url = f"https://{oneviewip}/rest/server-hardware"
headers = {
        'Auth': auth_token,
        'X-Api-Version': '3000', #oneview version 6.30 --> 'x-api-key': '3200' 6.20 -->'x-api-key': '3000'
        'Content-Type': 'application/json'
        }

print(f"The number of Hosts that is being added:{len(hostList)}")
print("Hosts ilo IP addresses",hostList)
for ip in hostList:
    try:
        print("================================================================================")
        print(ip,":is starting to being added")
        payload = json.dumps({
        "hostname": ip,
        "username": "admin",# username that is used to enter iLO
        "password": "XXXXXXX",#password that is used to enter iLO
        "force": False,
        "licensingIntent": "OneView",
        "configurationState": "Managed" #Managed or monitor, see oneview docs for more details
        })
        
        response = requests.request("POST", url, headers=headers, data=payload,verify=False)
        #print(response.text)
        time.sleep(1)

    except:
        print(ip,"error")


print("Script is done and servers are added but just wait for oneview tasks to finish completely.")