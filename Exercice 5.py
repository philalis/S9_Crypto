import json as json
import base64 as base64
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256


input =  json.load(open("Ex5_input.json"))

def main():
    salt = base64.b64decode(input["salt"])
    password = "123PetitsChats"
    keys = PBKDF2(password, salt, 64, count=6000000, hmac_hash_module=SHA256)
    print(keys)

    pass











if __name__ == '__main__':
    main()