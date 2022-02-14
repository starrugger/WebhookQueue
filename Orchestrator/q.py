from authentication import authenticationForQueue
import requests, json

def ListQ():
    sesh=requests.session()
    auth=authenticationForQueue()
    sesh.headers.update(auth)
    thing=sesh.request(method='get', url="https://mckatlautomation.mckenneys.com/odata/QueueDefinitions/")
    odata=thing.json()['value']
    for thing in odata:
        print(thing['Name'])

def ListRobots():
    sesh=requests.session()
    auth=authenticationForQueue()
    sesh.headers.update(auth)
    thing=sesh.request(method='get', url="https://mckatlautomation.mckenneys.com/odata/Robots/")
    odata=thing.json()['value']
    for thing in odata:
        print(thing)
    # response= requests.Session()

    # #Header
    # newHeaders = {'Content-Type': 'application/json'}
    # #creating pyDict holding necessary login Model
    # payload={'tenancyName': 'Default','usernameOrEmailAddress': 'Assessor','password': '12345abcde'}

    # response.headers.update(newHeaders)
    # #sending the post request. data is DUMPED and sent as a JSON file to fit orchestrator parameters
    # thing=response.request(method='post', url="https://mckatlautomation.mckenneys.com/api/Account/Authenticate", data=json.dumps(payload))
    # #retrieving the file as a json
    
    # reply=thing.json()
    # newHeaders={'Authorization': 'Bearer '+reply['result'], 'accept': 'application/json'} 

    # print(newHeaders)
    # response.headers.update(newHeaders)
    # thing=response.request(method='get', url="https://mckatlautomation.mckenneys.com/odata/QueueDefinitions/")
    # print(thing.text)
    # print(thing.status_code)
    
    # print(thing.content)
    # print(thing.headers)
    




print(ListRobots())
