from authentication import authentication, authenticationForStartJob
from ProcessKey import processKey
import requests, json


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
#response.close()
io={'Authorization': 'Bearer '+reply['result']} 

headers=response.headers.update(io)

text=response.request(method='get', url="https://mckatlautomation.mckenneys.com/odata/Robots")
print(str(response.headers))
print(str(text.json()))


response.close()


# key= processKey(processName, sesh)
# print(key)
# sesh.close()

# sesh=requests.session()
# headers=authenticationForStartJob()
# sesh.headers.update(headers)
# print(StartJob.StartJob("KnowBe4Upload_Production2"))