import bencodepy

def parse_torrent_file(file_path):
    with open(file_path, "rb") as f:
        torrent_data = bencodepy.decode(f.read())
    return torrent_data

# Example usage
if __name__ == "__main__":
    import sys
    torrent_file = sys.argv[1]
    print(parse_torrent_file(torrent_file))
