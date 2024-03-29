# With this scripts, Server Profile Template can be created.
# The settings that is mentioned in payload needs to be checked and edited accordingly your needs and servers.
# For exmaple, in this example I am giving below "serverHardwareTypeUri": "/rest/server-hardware-types/520A0FDD-D3F4-48A4-8363-2EE759242936" represents DL 360 Gen 10 Plus servers.
# Since it is hard to know all settings, it makes sense to first an example server profile template or server profile is created through Oneview UI and can be exported to see the attributes.
# But I still highly recommend to create Server Profile Template within Oneview UI for your needs, since it is not repetitive task as others.
# @author Mustafa Yıldırım

import requests
import json
import urllib3
urllib3.disable_warnings() #With this statement, SSL warnings that is being received everytime the script is run is ignored.

#==========================================Variables that needs to be edited accordingly your environment==========================================================
oneviewip="10.X.X.X" #Oneview IP Address 
auth_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Authenticatin token that is generated by "getAuthToken.py" in this repo or via POST login-sessions API call
serverprofileTemplateName="DENEME" #name for Server Profile Template

#===================================================================================================================================

url = f"https://{oneviewip}/rest/server-profile-templates"
headers = {
  'Auth': auth_token,
  'X-Api-Version': '3000', #oneview version 6.30 --> 'x-api-key': '3200' 6.20 -->'x-api-key': '3000'
  'Content-Type': 'application/json'
}


payload = json.dumps({
  "type": "ServerProfileTemplateV8",
  "name": serverprofileTemplateName, #name specified above
  "description": "Profil that is being used by DL360 Gen10 Plus 1", 
  "serverProfileDescription": "",
  "serverHardwareTypeUri": "/rest/server-hardware-types/520A0FDD-D3F4-48A4-8363-2EE759242936", #Attention: server hardware type uri that changes according to server hardware type e.g DL360, DL 380 Gen10 or Gen 10 plus
  "enclosureGroupUri": None,
  "affinity": None,
  "hideUnusedFlexNics": None,
  "macType": "Physical",
  "wwnType": "Physical",
  "serialNumberType": "Physical",
  "iscsiInitiatorNameType": "AutoGenerated",
  "osDeploymentSettings": None,
  "firmware": {
    "complianceControl": "Unchecked",
    "manageFirmware": False,
    "forceInstallFirmware": False
  },
  "connectionSettings": {
    "complianceControl": "Unchecked",
    "manageConnections": False,
    "connections": []
  },
  "bootMode": {
    "complianceControl": "Checked",
    "manageMode": True,
    "mode": "UEFIOptimized",
    "pxeBootPolicy": "Auto",
    "secureBoot": "Unmanaged"
  },
  "boot": {
    "complianceControl": "Unchecked",
    "manageBoot": False,
    "order": []
  },
  "bios": {
    "complianceControl": "Checked",
    "manageBios": True,
    "overriddenSettings": [
      {
        "id": "WorkloadProfile",
        "value": "Virtualization-MaxPerformance"
      },
      {
        "id": "MinProcIdlePower",
        "value": "NoCStates"
      },
      {
        "id": "IntelUpiPowerManagement",
        "value": "Disabled"
      },
      {
        "id": "SubNumaClustering",
        "value": "EnableSnc2"
      },
      {
        "id": "MinProcIdlePkgState",
        "value": "NoState"
      },
      {
        "id": "EnergyPerfBias",
        "value": "MaxPerf"
      },
      {
        "id": "UncoreFreqScaling",
        "value": "Maximum"
      },
      {
        "id": "PowerRegulator",
        "value": "StaticHighPerf"
      },
      {
        "id": "CollabPowerControl",
        "value": "Disabled"
      },
      {
        "id": "DynamicIntelSpeedSelectMode",
        "value": "Disabled"
      },
      {
        "id": "EnergyEfficientTurbo",
        "value": "Disabled"
      },
      {
        "id": "NumaGroupSizeOpt",
        "value": "Clustered"
      }
    ]
  },
  "managementProcessor": {
    "complianceControl": "Unchecked",
    "manageMp": False,
    "mpSettings": []
  },
  "localStorage": {
    "complianceControl": "Unchecked",
    "sasLogicalJBODs": [],
    "controllers": []
  },
  "sanStorage": {
    "complianceControl": "Unchecked",
    "manageSanStorage": False,
    "sanSystemCredentials": [],
    "volumeAttachments": []
  }
})


response = requests.request("POST", url, headers=headers, data=payload)

print("script is done here response text:")
print(response.text)
