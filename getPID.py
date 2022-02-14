from subprocess import Popen, PIPE

def getPid():
    p = Popen(['netstat','-ao'], stdout=PIPE).stdout.readlines()
    i=0
    bucket=""
    while i<len(p):
        input=str(p[i])
        i+=1
        if "127.0.0.1:1024" in input:
            bucket+=input

    netstat=bucket.split()
    assert len(netstat)>0 

    netstat=bucket.split()

    #pid given that we are thin the LOCALLLL environment
    pid=netstat[len(netstat)-1].strip("\\r\\n'")
    return(pid)

