from hashlib import sha1

from Crypto.Util.number import bytes_to_long, inverse

message = b"qwwerty"
message2 = b"asdfgh"

print("message: ", message.hex())
print("message2: ", message2.hex())

h1 = bytes_to_long(sha1(message).digest())
h2 = bytes_to_long(sha1(message2).digest())

s1 = int(input("s1: "))
s2 = int(input("s2: "))

q = int(input("q: "))
g = int(input("g: "))
p = int(input("p: "))

numerator = (h1 - h2) % q
denominator = (s1 - s2) % q

k = (numerator * inverse(denominator, q)) % q
x = inverse(k, q)
print("k:",k)
r = pow(g, k, p) % q
print("r :",r)
token = input("token: ").encode()
h = bytes_to_long(sha1(token).digest())
s = inverse(k, q) * (h + x * r) % q

print("token(hex):", token.hex())
print(f"{r}, {s}")