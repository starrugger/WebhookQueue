from pyngrok import ngrok as n
import sys


def startTunnel(incomingPort=None):
    if incomingPort==None:
        tunnel = n.connect(1024,'http',"-bind-tls=true")
    else:
        tunnel = n.connect(int(incomingPort),'http',"-bind-tls=true")

    secureURI=""
    #gettings https tunnel
    for tun in n.get_tunnels():
        if 'https' in tun.public_url:
            secureURI=tun.public_url

    with open('./url.txt','w') as a:
        a.write(secureURI)
   
    a.close()
    ngrok_process = n.get_ngrok_process()
    ngrok_process.proc.wait()
    return n
    



    #old way of running server and killing through ctrl c
    # try:
    #     # Block until CTRL-C or some other terminating event
    #     ngrok_process.proc.wait()
        
    # except (KeyboardInterrupt, ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as a:
    #     print(" Shutting down server.")
    #     n.kill()

if __name__=='__main__':
    if len(sys.argv)>1:
        startTunnel(sys.argv[1])
        
    else:
        try:
        # Block until CTRL-C or some other terminating event
            n=startTunnel()
        
        except (KeyboardInterrupt, ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as a:
            print(" Shutting down server from ngrok")
            n.kill()
        