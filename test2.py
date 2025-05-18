import struct

def F(x, y, z): return (x & y) | (~x & z)
def G(x, y, z): return (x & z) | (y & ~z)
def H(x, y, z): return x ^ y ^ z
def I(x, y, z): return y ^ (x | ~z)

def left_rotate(x, n):
    x &= 0xFFFFFFFF
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

S = [7, 12, 17, 22]*4 + [5, 9, 14, 20]*4 + [4, 11, 16, 23]*4 + [6, 10, 15, 21]*4
K = [int(abs(__import__('math').sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

def index(i):
    if 0 <= i < 16: return i
    elif 16 <= i < 32: return (5 * i + 1) % 16
    elif 32 <= i < 48: return (3 * i + 5) % 16
    else: return (7 * i) % 16

def md5_padding(msg_len_bytes):
    pad = b'\x80'
    while (msg_len_bytes + len(pad)) % 64 != 56:
        pad += b'\x00'
    bit_len = msg_len_bytes * 8
    pad += struct.pack('<Q', bit_len)
    return pad

def md5_from_state(state_bytes, count_bytes, new_data):
    a, b, c, d = struct.unpack("<4I", state_bytes)
    message = new_data + md5_padding(count_bytes + len(new_data))
    for i in range(0, len(message), 64):
        M = list(struct.unpack("<16I", message[i:i+64]))
        A, B, C, D = a, b, c, d
        for j in range(64):
            if j < 16: f = F(B, C, D)
            elif j < 32: f = G(B, C, D)
            elif j < 48: f = H(B, C, D)
            else: f = I(B, C, D)
            f = (f + A + K[j] + M[index(j)]) & 0xFFFFFFFF
            A, B, C, D = D, (B + left_rotate(f, S[j])) & 0xFFFFFFFF, B, C
        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF
    return struct.pack("<4I", a, b, c, d).hex()

original_message = b"Dreamhack"
new_data = b"a"
secret_len = 500

key = b"A"*secret_len
original_hash = "764e0c568ca4c990802290cb3fd05f93"

state_bytes = bytes.fromhex(original_hash)

padding = md5_padding(secret_len + len(original_message))
forged_message = original_message + padding + new_data
forged_hash = md5_from_state(state_bytes, secret_len + len(original_message) + len(padding), new_data)

forged_message_hex = forged_message.hex()
forged_hash_hex = forged_hash

print(forged_message_hex)
print(forged_hash_hex)
