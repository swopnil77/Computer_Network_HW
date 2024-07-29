from peer import Peer

class Downloader:
    def __init__(self, peers):
        self.peers = [Peer(ip, port) for ip, port in peers]

    def download(self):
        for peer in self.peers:
            peer.connect()
            # Implement the logic for requesting and downloading pieces

# Example usage
if __name__ == "__main__":
    peers = [("127.0.0.1", 6881)]
    downloader = Downloader(peers)
    downloader.download()
