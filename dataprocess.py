"""process data and contents"""

import simplejpeg

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64




def generate_key(password, hash_salt):

    generated_key = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=hash_salt,
        iterations=100000,
        )

    key = base64.urlsafe_b64encode(generated_key.derive(password))

    return key
