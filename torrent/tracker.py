import requests
from urllib.parse import urlencode

def get_peers_from_tracker(torrent_data, port):
    announce_url = torrent_data[b'announce'].decode('utf-8')
    info_hash = torrent_data[b'info']
    peer_id = b"-PC0001-" + bytearray([i % 256 for i in range(20)])
    
    params = {
        'info_hash': info_hash,
        'peer_id': peer_id,
        'port': port,
        'uploaded': 0,
        'downloaded': 0,
        'left': 0,
        'compact': 1
    }

    url = f"{announce_url}?{urlencode(params)}"
    response = requests.get(url)
    return response.content

# Example usage
if __name__ == "__main__":
    import sys
    from torrent_parser import parse_torrent_file
    torrent_file = sys.argv[1]
    torrent_data = parse_torrent_file(torrent_file)
    print(get_peers_from_tracker(torrent_data, 6881))
