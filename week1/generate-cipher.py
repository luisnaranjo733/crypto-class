import sys
from pprint import pprint

MSGS = (
    'loga',
    'log a'
)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    hex_encoded = c.encode('hex')
    print 'Encoding "%s" to "%s"' % (msg, hex_encoded)
    return c

key = random(1024)
# print(key)
ciphertexts = [encrypt(key, msg) for msg in MSGS]

# pprint(ciphertexts)