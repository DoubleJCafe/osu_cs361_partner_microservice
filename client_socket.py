import zmq
import json

context = zmq.Context()

# socket to talk to server

print("connecting to remote jobs server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

variable = 'python'

# do something
socket.send(json.dumps(variable).encode("utf-8"))
print("sent request")

message = json.loads(socket.recv().decode('utf-8'))
print('waiting for respsonse')

with open('jobs.txt', 'r') as f:
    print_this = f.read()
    print_this = print_this.replace("\\n", "\n")
    print(print_this)
    f.close()
