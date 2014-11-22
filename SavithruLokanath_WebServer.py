*****HTTP Web Server Implementation Using Sockets*****

import socket
from socket import *                                   #Import libraries
import thread
from time import ctime
import os
import os.path
 
host = ''                                              #Defines the ip adress of the host
port = 9600
                                                       #Defines the port number
size = 1024                                            #Defines the size of the blocks that the host can accept

def response():
    return 'SOCKET SERVER'               

#ACCEPT REQUEST FROM CLIENT SOCKET

def handler(client,address):                                                 
    while 1:
        data = client.recv(size)                                   
        print 'data:' + repr(data)
        a,b,c = data.split(" ")[0:3]                   #Splitting the request & storing in 'a,b,c' variables 
        #print a
        #print b
        #print c

 #ERROR HANDLING THE REQUESTS

        if (data and a != 'GET'):   
            client.send('HTTP/1.1 400 OK\n Content-Type: text/html \n\n <HTML> <h1> Invalid Request Method</h1> </HTML>')
            if (data and c != 'HTTP/1.1'):
                client.send('HTTP/1.1 400 OK\n Content-Type: text/html \n\n <HTML> <h1> Invalid HTTP Version</h1> </HTML>')
                
        else:

            t = b.split(".")                                #Splitting the URL & storing it in variable 't'
            #print t
            #print t[0]
            #print t[1]

#ERROR HANDLING IN THE URL RECEIVED            

            if t[1] not in config['format']:                #Check File Format
                client.send('HTTP/1.1 501 OK\n Content-Type: text/html \n\n <HTML> <h1> 501 : File Type Not Supported</h1> </HTML>') 
                break
            
            bb = b.split("/")                                                   
            req = bb[1]
            print req + 'xxx'                                                                

            if '*' in req:                                  #Check URL contains any Special Characters like '*' '$' and send errors            
                client.send('HTTP/1.1 400 OK\n Content-Type: text/html \n\n <HTML> <h1> Invalid URL</h1> </HTML>')
                break
            if '%' in req:
                client.send('HTTP/1.1 400 OK\n Content-Type: text/html \n\n <HTML> <h1> Invalid URL</h1> </HTML>')
                break


            if not os.path.isfile(bb[1]):                   #Check if file present in the home directory
                print os.path.isfile(b)
                client.send('HTTP/1.1 404 OK\n Content-Type: text/html \n\n <HTML> <h1> Error 404 : File Not Found</h1> </HTML>')
 
 #SERVE THE REQUESTED FILE

            if t[1] == 'jpg':
                    info = open(req,'rb')
                    image_data = info.read()
                    client.send('HTTP 1.0 200 OK\nContent-Type: image/jpg \n\n' + image_data)
                    exit
            elif t[1] == 'gif':
                    info = open(req, 'rb')
                    image_data = info.read()
                    client.send('HTTP 1.0 200 OK\nContent-Type: image/gif \n\n' + image_data)
                    exit
            elif t[1] == 'txt':
                    info = open(req, 'rb')
                    image_data = info.read()
                    client.send('HTTP 1.0 200 OK\nContent-Type: text/txt \n\n' + image_data)
                    exit
            elif t[1] == 'html':
                    info = open(req, 'rb')
                    image_data = info.read()
                    client.send('HTTP 1.0 200 OK\nContent-Type: text/html \n\n' + image_data)
                    exit
            
        if not data:break                                  #If no data received from the client then close the socket
        client.close()

    else:
        client.send('HTTP/1.1 500 OK\n Content-Type: text/html \n\n <HTML> <h1> Internal Server Error: Cannot Allocate Memory</h1> </HTML>')

#MULTI-THREADING TO ESTABLISH CONTACT WITH MULTIPLE USERS 
 
if __name__=='__main__':
    ADDR = (host, port)
    s = socket(AF_INET, SOCK_STREAM)                   
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)                                           #Binds the socket (server to the client) & establishes connection
    s.listen(5)                                     
    while 1:
        print 'Awaiting connection'
        client, address = s.accept()
        print 'Server Connected To:', address
        thread.start_new_thread(handler, (client, address)) 
    client.close()
