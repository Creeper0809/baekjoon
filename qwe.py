P1 = bytes.fromhex('00' * 16)
P2 = bytes.fromhex('00' * 16)
P3 = bytes.fromhex('01' * 16)
P4 = bytes.fromhex('02' * 16)

a = P1+P2+P3+P4
print(a.hex())