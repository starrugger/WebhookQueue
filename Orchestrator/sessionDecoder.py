def Decode(response, Print=False):

    try:
        body=response.json()
        # count=body['@odata.count']
        
        data=body['value']
        
        if Print:
            header=response.headers
            print("*************Headers*************")
            print(header)
            print()
            print
            for item in data:
                print(item)
                print()
            
        return data
    except ValueError:
        print(response.text)