##Вариант 2
from generation_key import generation_key, encryption_key
from encryption import encryption
from decryption import decryption
import json
import os

if __name__ == '__main__':
    settings = {
        'initial_file': 'text.txt',
        'encrypted_file': 'encrypted.txt',
        'decrypted_file': 'decrypted.txt',
        'symmetric_key': 'symmetric_key.txt',
        'public_key': 'public_key.pem',
        'private_key': 'private_key.pem',

    }
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)
    with open('settings.json') as json_file:
        json_data = json.load(json_file)

    iv = os.urandom(16)

    while True:
        print("1. Generate keys")
        print("2. Encrypt text")
        print("3. Decrypt text")
        cmd = input("Chose action: ")
        if cmd == "1":
            while True:
                print("Select size: ")
                print("1. 128 bit")
                print("2. 192 bit")
                print("3. 256 bit")
                cmd_2 = input("Select the key length: ")
                if cmd_2 == "1":
                    generation_key(settings, 16)
                    encryption_key(settings)
                    break
                elif cmd_2 == "2":
                    generation_key(settings, 24)
                    encryption_key(settings)
                    break
                elif cmd_2 == "3":
                    generation_key(settings, 24)
                    encryption_key(settings)
                    break

        elif cmd == "2":
            encryption(settings, iv)

        elif cmd == "3":
            decryption(settings, iv)
        else:
            print("Incorrect value")