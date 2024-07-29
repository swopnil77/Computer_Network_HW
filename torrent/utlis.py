import hashlib

def calculate_hash(data):
    return hashlib.sha1(data).digest()

# Example usage
if __name__ == "__main__":
    data = b"Hello, World!"
    print(calculate_hash(data))
