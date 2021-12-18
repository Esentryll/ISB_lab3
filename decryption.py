from generation_key import decryption_key
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decryption(setting: dict, iv: bytes):
    """ Функция дешифрования текста """

    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)

    with open(setting['encrypted_file'], mode='rb') as dc_file:
        enc_text = dc_file.read()

    cipher = Cipher(algorithms.Camellia(ds_key), modes.CBC(iv))
    decrypter = cipher.decryptor()
    dc_text = decrypter.update(enc_text) + decrypter.finalize()
    unpad = pd.ANSIX923(128).unpadder()
    unpadded_dc_text = unpad.update(dc_text) + unpad.finalize()
    res = unpadded_dc_text.decode('UTF-8')
    print("Decryption text:")
    print(res)

    with open(setting['decrypted_file'], 'w') as dec_file:
        dec_file.write(res)