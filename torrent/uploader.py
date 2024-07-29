from peer import Peer

class Uploader:
    def __init__(self, peers):
        self.peers = [Peer(ip, port) for ip, port in peers]

    def upload(self):
        for peer in self.peers:
            peer.connect()
            # Implement the logic for sending pieces

# Example usage
if __name__ == "__main__":
    peers = [("127.0.0.1", 6881)]
    uploader = Uploader(peers)
    uploader.upload()
