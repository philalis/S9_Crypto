import json as json
import base64 as base64
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
from Cryptodome.Hash import SHA512


input_json =  json.load(open("Ex5_input.json"))

def main():
    salt = base64.b64decode(input_json["salt"])
    password = "123PetitsChats"
    #keys = PBKDF2(password, salt, 32, count=6000000, hmac_hash_module=SHA256)
    #print(keys)


    mnemonic_phrase = input("Enter the mnemonic phrase: ")
    salt = base64.b64decode("mnemonic")
    keys = PBKDF2(mnemonic_phrase, salt, 64, count=2048, hmac_hash_module=SHA512)
    print(keys)
    pass











if __name__ == '__main__':
    main()