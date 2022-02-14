import sys
sys.path.append("C:\\Users\\nivinadmin\\Documents\\MCKWebhook\\WebServer\\Orchestrator\\")
from authentication import authentication, authenticationForStartJob
from ProcessKey import processKey
import requests, json

def StartJob(processName, jobPriority=None):
    if jobPriority==None:
        jobPriority=='Normal'
    sesh=requests.session()
    headers=authentication()
    sesh.headers.update(headers)
    # print(headers)

    key= processKey(processName, sesh)
    print(key)
    sesh.close()

    sesh=requests.session()
    headers=authenticationForStartJob()
    sesh.headers.update(headers)
    print("Successful got the processKey and Got the authentication to start the Job")
    payload = {
    "startInfo":{
        "ReleaseKey":key,
        "Strategy": "RobotCount",
        "RobotIds":[],
        "NoOfRobots":1, 
        "Source": "Manual",
        "JobPriority":jobPriority
        }
    }
    print(type(payload))
    #this is the LiveRPA folder always going to be 1
    newHeaders={'X-UIPATH-OrganizationUnitId': '1'}

    sesh.headers.update(newHeaders)
    #print(sesh.headers.values())

    thing=sesh.request(method='post', url="https://mckatlautomation.mckenneys.com/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs/", data=json.dumps(payload))
    print(thing.text)
    print(thing.status_code)
    # print(thing.content)
    # print(thing.headers)
    




print(StartJob("KnowBe4Upload_Production2"))
