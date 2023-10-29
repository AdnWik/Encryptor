from encryptor import Encryptor


class MySecret:

    def __init__(self) -> None:
        self.encryptor = Encryptor()
        self.safe_context = ''

    def encrypt_file(self, file):
        pass

    def encrypt_folder(self, folder):
        pass

    def decrypt_file(self, file):
        pass

    def decrypt_folder(self, folder):
        pass
