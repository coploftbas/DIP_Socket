# Echo client program
import socket, sys, getopt

#HOST = '127.0.0.1'
HOST = 'olaf.snu.ac.kr'  # The remote host
PORT = 8080        # The same port as used by the server

def main(argv):
    pattern = ''
    try:
        opts, args = getopt.getopt(argv,"hrs")
    except getopt.GetoptError:
        print 'socket_client.py -h'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py <access type>'
            print '<access type> : -s -> for sequential'
            print '              : -r -> for random'
            sys.exit()
        elif opt in ("-s"):
            pattern = 0 #SEQUENTIAL
        elif opt in ("-r"):
            pattern = 1 #RANDOM

    #make socket connection to server
    print "Connecting to server..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print "Connect to server complete !!"

    print "Sending file to server for writing..."
    myFile = open("simple.db","rb")
    while True:
        val = myFile.read(1028)
        if not val:
            break
        #print "Client send to write :: " + val
        s.send(val)
    myFile.close()
    print "Complete sending file for writing !!"
    
    #SEQUENCTIAL
    if pattern == 0 :
        #SEND DBGEN TO SERVER && SEND TRACGER_SEQ TO SERVER
        print "Sending sequential pattern to server..."
       
        myFile = open("trace-seq.txt","r")
        for line in myFile.readlines():
            val = line.split()
            #print "Client send - " + val[0]
            s.send(val[0])
            data = s.recv(1024)
            #print 'Received data :: '+ data
        myFile.close()        
        
    #RANDOM    
    else: 
        #SEND DBGEN TO SERVER && SEND TRACGER_SEQ TO SERVER        
        print "Sending random pattern to server & retrieving data from server..."
        
        myFile = open("trace-ran.txt","r")
        for line in myFile.readlines():
            val = line.split()
            #print "Client send - " + val[0]
            s.send(val[0])
            data = s.recv(1024)
            #print 'Received data :: '+ data
        myFile.close()
    
    print "Complete retreiving data from server !!"
    s.close()
    print "Connection to server is closed !!"
        
if __name__ == "__main__":
    main(sys.argv[1:])
