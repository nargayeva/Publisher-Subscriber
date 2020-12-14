import zmq, os, time

context = zmq.Context()
s = context.socket(zmq.PUB)
p = 'tcp://127.0.0.1:2000'
s.bind(p)

name = input("Enter your folder name: ");

for i in os.listdir(name):
    s.send_string(f"Folder {name} has {i}")
    time.sleep(1)
