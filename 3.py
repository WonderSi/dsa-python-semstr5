import hashlib

hash = hashlib.sha256()

hash.update(b"Nobody inspects")

print(hash.hexdigest())