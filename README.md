TCP_Server
==========

A Multi-Threaded HTTP based Web Server 

*** README ***

NAME : SAVITHRU M LOKANATH

SOURCE FILE : SavithruLokanath_WebServer.py

MULTI-THREADING ENABLED

Steps to implement a HTTP web server on your local machine - 

1) OPEN the source file SavithruLokanath_WebServer.py using any python interpreters or RUN this command - 
   python SavithruLokanath_WebServer.py in terminal
 
2) The port number is set to 9600 initially. CHANGE to a value greater than 8000 if needed

3) Once the source file is running, OPEN any browser (MOZILLA FIREFOX, GOOGLE CHROME, APPLE SAFARI) and TYPE - localhost:(Port     Number)
   Ex. localhost:9600
   You will now land on the default page
   
4) If you need to ACCESS the files stored in the server, simply mention the path after the port number in the above statement
   Ex. If you want to access a file test.txt which is stored in Assignment-SavithruLokanath in your local storage
       Type in : localhost:9600/test.txt
       
5) This will RETURN the contents of the test.txt file

6) Similarly you can access other files stored in the local directory

7) Multi-Threading can be tested by opening another session with the server on a different browser
