# This script helps to generate AUTH token for the oneviews that username and password have given.
# this AUTH token is necessary for REST API calls to oneview.
# In order to generate the token, POST /rest/login-sessions API needs to be used.
# @author Mustafa Yıldırım

import urllib3
import requests
import json
urllib3.disable_warnings() #With this statement, SSL warnings that is being received everytime the script is run is ignored.

#==========================================Variables that needs to be edited accordingly your environment==========================================================
oneview_ip_list=['10.84.8.95','10.84.8.93']#The Oneview IP list.
oneview_password="PUT YOUR PASSWORD HERE"
oneview_username="administrator"#oneview username (keep in mind that if the task that is going to be done through this token needs admin priviliges, then user that we get token with it needs to have admin priviliges.)
head1 = {'x-api-key': '3200','Content-Type': 'application/json', } #headers, #oneview version 6.30 --> 'x-api-key': '3200' 6.20 -->'x-api-key': '3000'
#===================================================================================================================================


data1=json.dumps{"authLoginDomain":"local",#Data needs to be given as JSON object not regular dictinary

    "password": oneview_password,

    "userName": oneview_username} #data body




oneview_Auth_dict={}
for i in oneview_ip_list:

    url=f'https://{i}/rest/login-sessions'
    #print(url)

    r=requests.post(url, headers=head1, data=data1 ,verify=False) #with verify=False  "SSL connection check error" is skipped.

    print(i,r.json()['sessionID'])

    oneview_Auth_dict[i]=r.json()['sessionID']


print(oneview_Auth_dict)

print("Done.")
