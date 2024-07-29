import socket

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def send_message(self, message):
        self.socket.sendall(message)

    def receive_message(self):
        return self.socket.recv(4096)

# Example usage
if __name__ == "__main__":
    peer = Peer("127.0.0.1", 6881)
    peer.connect()
    peer.send_message(b"Hello, Peer!")
    print(peer.receive_message())
