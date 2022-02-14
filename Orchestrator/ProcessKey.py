from authentication import authentication as auth
import requests, json
from sessionDecoder import Decode


def processKey(Name, sesh):
    #testurl="https://mckatlautomation.mckenneys.com/odata/Releases?%24filter=Name%20eq%20'Cylance_Report_Production2'"
    api_Call_Url="https://mckatlautomation.mckenneys.com/odata/Releases?$filter=Name eq '{name}'".format(name=Name)

    processes=sesh.request(method='get', url=api_Call_Url)
    
    response=Decode(processes)
    
    for everything in response:
        if everything.get('Key'):
            key=everything.get('Key')
    
    return key