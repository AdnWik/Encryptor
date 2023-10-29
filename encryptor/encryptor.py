from os import getenv
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class Encryptor:

    def __init__(self) -> None:
        load_dotenv()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=getenv('SALT').encode('utf-8'),
            iterations=480000
            )
        self.token = Fernet(
            base64.urlsafe_b64encode(
                kdf.derive(getenv('PASSWORD').encode('utf-8'))
                )
            )

    def encrypt(self, content):
        safe_content = self.token.encrypt(content.encode('utf-8'))
        return safe_content

    def decrypt(self, safe_content):
        decoded_content = self.token.decrypt(safe_content).decode('utf-8')
        return decoded_content
