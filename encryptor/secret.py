import os
import logging
from shutil import rmtree
from crypto import Encryptor


class MySecret:

    def __init__(self) -> None:
        self.crypto = Encryptor()
        self.safe_context = ''

    def encrypt_file(self, args, target):
        print(args)
        file = args.file.split("\\")
        print(file)
        if os.path.exists(target):
            rmtree(target)

        os.mkdir(f'{target}')
        with open(args.file, 'r', encoding='utf-8') as file_unsafe:
            context = file_unsafe.read()
            self.safe_context = self.encrypt_content(context)
            logging.debug('Original content: %s', context)
            logging.debug('Safe content: %s', self.safe_context)

        with open(f'{target}/{file[-1]}', 'w', encoding='utf-8') as file_safe:
            file_safe.write(self.safe_context)

    def encrypt_folder(self, args, target):
        if os.path.exists(target):
            rmtree(target)

        for path, directories, files in os.walk(args.folder):
            if path.startswith(".."):
                new_path = path[2:]
            os.makedirs(f'{target}/{new_path}')
            for file in files:
                with open(f'{path}/{file}', 'r', encoding='utf-8') as file_unsafe:
                    context = file_unsafe.read()
                    self.safe_context = self.encrypt_content(context)
                    logging.debug('Original content: %s', context)
                    logging.debug('Safe content: %s', self.safe_context)

                with open(f'{target}/{new_path}/{file}', 'w', encoding='utf-8') as file_safe:
                    file_safe.write(self.safe_context)

    def decrypt_file(self, file):
        pass

    def decrypt_folder(self, folder):
        pass

    def encrypt_content(self, content):
        safe_content = self.crypto.encrypt(content)
        safe_content = safe_content.decode('utf-8')
        return safe_content

    def decrypt_content(self, content):
        unsafe_content = self.crypto.decrypt(content)
        return unsafe_content
