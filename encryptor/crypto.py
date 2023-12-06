from os import getenv
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class Crypto:

    def __init__(self, path, password) -> None:
        load_dotenv()
        self.path = path
        self.password = password

    def crete_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=getenv('SALT').encode('utf-8'),
            iterations=480000
            )
        key = base64.urlsafe_b64encode(
            kdf.derive(self.password.encode('utf-8')))
        return key


class Encrypt(Crypto):
    def __init__(self, path, password) -> None:
        super().__init__(path, password)

    def execute(self):
        with open(self.path, 'r') as file:
            data_to_encrypt = file.read()

        fernet = Fernet(self.crete_key())
        encrypted_content = fernet.encrypt(data_to_encrypt.encode('utf-8'))

        with open(self.path.rename(self.path.with_suffix('.code_aw')), 'w') as file:
            file.write(encrypted_content.decode('utf-8'))


class Decrypt(Crypto):
    def __init__(self, path, password) -> None:
        super().__init__(path, password)

    def execute(self):
        with open(self.path, 'r') as file:
            data_to_decrypt = file.read()

        fernet = Fernet(self.crete_key())
        decrypted_content = fernet.decrypt(data_to_decrypt)

        with open(self.path.rename(self.path.with_suffix('.txt')), 'w') as file:
            file.write(decrypted_content.decode('utf-8'))


class Append(Crypto):
    def __init__(self, path, password, data_to_append) -> None:
        super().__init__(path, password)
        self.data_to_append = data_to_append

    def execute(self):
        fernet = Fernet(self.crete_key())

        with open(self.path, 'r') as file:
            content = file.read()
            content = fernet.decrypt(content).decode('utf-8')
            content += self.data_to_append
            content = fernet.encrypt(content.encode('utf-8'))

        with open(self.path, 'w') as file:
            file.write(content.decode('utf-8'))
