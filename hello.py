
import random
import binascii

def PRG(size):
    return ''.join([chr(random.randint(1, 127)) for x in range(size)])


message = 'hello world!'
key = PRG(len(message))


def encyrpt(key, message):
    key_b10 = [ord(char) for char in key]
    message_b10 = [ord(char) for char in message]

    cipher_b10 = []

    for k, m in zip(key_b10, message_b10):
        cipher_b10.append(k ^ m)

    return cipher_b10


cipher = encyrpt(key, message)
print(cipher)


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

bin_content = strxor('a', 'b')
content_as_bytes = bin_content.encode("utf-8")
decoded = bin_content.encode("utf-8").hex()
print(decoded)