import os
from config import DOWNLOAD_DIR

def save_piece(piece_index, piece_data):
    file_path = os.path.join(DOWNLOAD_DIR, f"piece_{piece_index}")
    with open(file_path, "wb") as f:
        f.write(piece_data)

def read_piece(piece_index):
    file_path = os.path.join(DOWNLOAD_DIR, f"piece_{piece_index}")
    with open(file_path, "rb") as f:
        return f.read()

# Example usage
if __name__ == "__main__":
    piece_data = b"Sample piece data"
    save_piece(0, piece_data)
    print(read_piece(0))
