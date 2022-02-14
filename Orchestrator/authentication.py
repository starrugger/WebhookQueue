import requests
import json

def authentication ():
    #created New session
    response= requests.Session()
    #Header
    newHeaders = {'Content-Type': 'application/json'}
    #creating pyDict holding necessary login Model
    payload={'tenancyName': 'Default','usernameOrEmailAddress': 'Assessor','password': '12345abcde'}

    response.headers.update(newHeaders)
    #sending the post request. data is DUMPED and sent as a JSON file to fit orchestrator parameters
    thing=response.request(method='post', url="https://mckatlautomation.mckenneys.com/api/Account/Authenticate", data=json.dumps(payload))
    #retrieving the file as a json
    reply=thing.json()
    #returning Authroization Dic type back. Note "Bearer " added before the Authentication value
    response.close()
    return {'Authorization': 'Bearer '+reply['result']} 

def authenticationForQueue():
    dict=authentication()
    bucket={'accept': 'application/json'}
    dict.update(bucket)
    return dict

def authenticationForStartJob ():
    dict=authentication()
    val=1
    # val.to_bytes(2, byteorder='big')
    bucket={'Content-Type': 'application/json','X-UIPATH-OrganizationUnitId': str(val) }
    dict.update(bucket)
    return dict

