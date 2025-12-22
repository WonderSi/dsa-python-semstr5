import hashlib

# Так как алгоритмы работают с байтами то и
# файл надо открывать на чтение байтов 'rb'
with open('3.py', 'rb') as f:
    hsh = hashlib.sha1()
    while True:
        data = f.read(2048)
        if not data:
            break
        hsh.update(data)
    rez = hsh.hexdigest()

print(rez)