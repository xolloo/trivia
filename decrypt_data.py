from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


# password = "1234"

with open("encrypt.bin", "rb") as file:
    private_key = RSA.import_key(open("private.pem", "rb").read(), passphrase=None)
    enc_session_key, nonce, tag, ciphertext = [file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(data.decode("utf-8"))