import zmq, time

context = zmq.Context()
s = context.socket(zmq.SUB)
p = 'tcp://127.0.0.1:2000'
s.connect(p)

s.setsockopt_string(zmq.SUBSCRIBE, '')
while True:
    receive = s.recv()
    print(receive)
    time.sleep(1)
