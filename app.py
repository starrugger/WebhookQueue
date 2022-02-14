# > set FLASK_APP=hello
# > flask run -h localhost -p 80
import json, datetime
from flask import Flask, request,make_response
from flask.json import jsonify
import sys
sys.path.append("C:\\Users\\nivinadmin\\Documents\\MCKWebhook\\WebServer\\")
from Orchestrator import StartJob



app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def reciever():
    
    #Verification 
    
    if request.method=='GET':
        try:
            print(StartJob.StartJob("KnowBe4Upload_Production2"))
            print("Job Started")
        except Exception:
            print("Job didn't Start")

        return app.make_response("Server Is UP. {}".format(datetime.datetime.now().strftime("%m%d%H%M%S")))
    else:
        #verifying if it is a challenge request
        challenge=request.headers.get("Smartsheet-Hook-Challenge")

        #if there is a challenge key
        if challenge !=None:

            #returning the challenge id back to Smartsheet for authorization
            response=make_response(jsonify({'smartsheetHookResponse':challenge}))
            return response

        #else you know it is a webhook message from Smartsheet
        else:
            #will get the body, and send a status code of 200
            body=request.data
            data=json.loads(body)

        
            webhookId=data['webhookId']
            time=datetime.datetime.now().strftime("%m%d%H%M%S")
#  chariot=gmail.GMail('A.User <nivinmck1@gmail.com>','Moreland30316')
 
            ##need to return webhookID 

            
            # try:
            #     StartJob.StartJob("KnowBe4Upload_Production2")
            #     print("Job Started")
            # except Exception:
            #     print("Job didn't Start")

            with open("./body{}.txt".format(time),'w') as f:
                f.write(str(type(body))+" "+str(data))
                f.close()

            response=make_response(("good",200))
            return response

if __name__=='__main__':
    if len(sys.argv)>1:
        print(sys.argv)
        app.run()
        app.run(host='localhost', port=int(sys.argv[1]), debug=True,FLASK_ENV="development") 
    else:
        app.run(host='localhost', port=1024)    
                    




    
