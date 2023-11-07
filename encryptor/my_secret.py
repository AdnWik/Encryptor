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

    def encrypt_content(self, content):
        safe_content = self.encryptor.encrypt(content)
        safe_content = safe_content.decode('utf-8')
        return safe_content

    def decrypt_content(self, content):
        unsafe_content = self.encryptor.decrypt(content)
        return unsafe_content
