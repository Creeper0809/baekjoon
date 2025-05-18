from Crypto.Cipher import AES

C1 = bytes.fromhex("1cdb44d4f72624855ce2255dc2081ea0")  # 예시
cipher = AES.new(b'\x00' * 16, AES.MODE_ECB)  # 더미 키로 ECB 복호화 객체 생성
key = cipher.decrypt(C1[:16])
print("Recovered key / IV:", key.hex())