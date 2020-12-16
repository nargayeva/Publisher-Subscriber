import zmq, time

context = zmq.Context()
socket = context.socket(zmq.SUB) # subscription socket
p = 'tcp://127.0.0.1:2000'  # where to communicate
socket.connect(p) # connecting to indicated server

socket.setsockopt_string(zmq.SUBSCRIBE, '') # subscribing
while True:
    receive = socket.recv() # receving the message
    print(receive.decode("utf-8")) # printing the received message and removing 'b
    time.sleep(1)
