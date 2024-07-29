import argparse
from torrent_parser import parse_torrent_file
from tracker import get_peers_from_tracker
from downloader import Downloader

def start_cli():
    parser = argparse.ArgumentParser(description="BitTorrent Client")
    parser.add_argument("torrent_file", help="Path to the .torrent file")
    args = parser.parse_args()

    torrent_data = parse_torrent_file(args.torrent_file)
    peers = get_peers_from_tracker(torrent_data, 6881)
    print(f"Peers: {peers}")

    downloader = Downloader(peers)
    downloader.download()

# Example usage
if __name__ == "__main__":
    start_cli()
