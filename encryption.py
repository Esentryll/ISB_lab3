from generation_key import decryption_key
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encryption(setting, iv):
    """ Функция шифрования текста """

    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)

    with open(setting['initial_file'], 'r', encoding='UTF-8') as f:
        res = f.read()
        print("The original text:")
        print(res)

    pad = pd.ANSIX923(128).padder()
    text = bytes(res, 'UTF-8')
    padded_text = pad.update(text) + pad.finalize()
    cipher = Cipher(algorithms.Camellia(ds_key), modes.CBC(iv))
    encryptr = cipher.encryptor()
    encryp_text = encryptr.update(padded_text) + encryptr.finalize()
    print("Encrypted text:")
    print(encryp_text)

    with open(setting['encrypted_file'], 'wb') as encryp_file:
        encryp_file.write(encryp_text)