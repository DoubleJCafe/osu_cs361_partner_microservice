import zmq
import json

context = zmq.Context()

# socket to talk to server

print("connecting to remote jobs server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

job_title = 'python'

# do something
socket.send(json.dumps(job_title).encode("utf-8"))
print("sent request")


message = json.loads(socket.recv().decode('utf-8'))
print('response received')
print(message)

