import zmq, os, time

context = zmq.Context()
socket = context.socket(zmq.PUB) # publisher socket
p = 'tcp://127.0.0.1:2000' # where to communicate
socket.bind(p) # binding socket to the address

name = input("Enter your folder name: "); # user input

for i in os.listdir(name): # looping through the files of the folder named "name"
    socket.send_string(f"Folder {name} has {i}") # publishing the message
    time.sleep(1)
