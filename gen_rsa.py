from Crypto.PublicKey import RSA

# password = "1234"

key = RSA.generate(4096)

private_key = key.export_key(passphrase=None, pkcs=8, protection="scryptAndAES128-CBC")
with open("private.pem", "wb") as file:
    file.write(private_key)

with open("pub.pem", "wb") as file:
    file.write(key.publickey().export_key())
