import random

def generate_custom_key(alphabet, custom_key):
    """
    Genera una clave personalizada que asocia cada caracter del alfabeto
    con otro caracter definido en la clave personalizada.
    """
    if len(alphabet) != len(custom_key):
        raise ValueError("El alfabeto y la clave personalizada deben tener la misma longitud")

    return dict(zip(alphabet, custom_key))

def encrypt(text, key):
    """
    Encripta un texto utilizando la clave proporcionada.
    """
    encrypted_text = ''
    for char in text:
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    """
    Desencripta un texto encriptado utilizando la clave proporcionada.
    """
    reversed_key = {v: k for k, v in key.items()}
    decrypted_text = ''
    for char in encrypted_text:
        if char in reversed_key:
            decrypted_text += reversed_key[char]
        else:
            decrypted_text += char
    return decrypted_text