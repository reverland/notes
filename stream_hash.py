reverland@LAPTOP-V5R287LO:~$ cat crypt.py
from Crypto.Hash import SHA256

with open('./6.1.intro.mp4_download', 'rb') as f:
    data = f.read()
print "len: ", len(data)
h = None
for i in range(0, len(data), 1024)[::-1]:
    hh = SHA256.new()
    c = data[i:i+1024]
    if h:
        c += h
    hh.update(c)
    h = hh.digest()
print hh.hexdigest()
