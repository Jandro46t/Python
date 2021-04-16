import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
print()
yazi = "Muzaffer"
fer = Fernet(key)
sifreli_yazi = fer.encrypt(yazi.encode())
print(sifreli_yazi)