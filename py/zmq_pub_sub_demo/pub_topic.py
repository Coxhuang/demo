import zmq
import time
from proto.demo_pb2 import Request


class Publisher(object):

    def __init__(self, topic):
        self.topic = topic
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("ipc://test.ipc")
        self.request = Request()
        self.request.name = "trunk"
        self.serialize_data = self.request.SerializeToString()

    def run(self):
        topic = bytes(self.topic,encoding = "utf8")
        while True:
            print(self.request)
            self.socket.send_multipart([topic, self.serialize_data])
            time.sleep(1)


if __name__ == '__main__':
    print("pub topic")
    pub = Publisher("/hello")
    pub.run()