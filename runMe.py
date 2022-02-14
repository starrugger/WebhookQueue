import subprocess as t
import sys as s
#getPID gets the process id of app listening on 1024 port
import getPID as g
from tunnelingOut import startTunnel as openUrl
import time


print(str(s.executable))

IDS=[]
#flask runnel
def runFlask():
    flaskRun=t.Popen(['powershell',s.executable, '.\\WebServer\\app.py'])
    time.sleep(5)
    FlaskProcessId=g.getPid()
    IDS.append(FlaskProcessId)
    print("FlaskProcessId {0}".format(str(FlaskProcessId)))

def runNgrok():
    ngrokRun=t.Popen(['powershell',s.executable, '.\\WebServer\\tunnelingOut.py' ])
    time.sleep(5)
    ngrokPID=g.getPid()
    IDS.append(ngrokPID)
    print("NgrokPID is {}".format(str(ngrokPID)))


runFlask()
runNgrok()
#nTunnel, currProc=openUrl()
print("Server started")
for things in IDS:
    print(things)
interaction=input("What do you want ('Stop' to stop)")

if interaction==("STOP" or KeyboardInterrupt):

    print(" Shutting down server.")
    
    t.run("tskill {0}".format(g.getPid()))  
 

   


# time.sleep(30)

# IDS.append(int(g.getPid()))
# print("The type returned from ngrok process is "+str(type(currProc)))
# print(currProc.kill())
# print("Ended Ngrok")
# for ids in IDS:
#     print("should have Stopped Server on port {0}".format(str(ids)))
#     t.run("tskill {0}".format(str(ids)))  


# print("should I run")
# ngrokRun.terminate()
# #flaskRun.kill()
