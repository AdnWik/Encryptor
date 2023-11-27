import argparse
import logging
import os
from shutil import rmtree
from my_secret import MySecret


def dir_path(string):
    logging.debug(f'STRING: {string}')
    if os.path.exists(string):
        return string
    else:
        #os.mkdir(string)
        raise (NotADirectoryError(string))


# INITIAL VALUES
LVL_MAPPING = {
    0: 50,  # CRITICAL
    1: 40,  # ERROR
    2: 20,  # INFO
    3: 10   # DEBUG
}

parser = argparse.ArgumentParser()
group_1 = parser.add_mutually_exclusive_group()
group_2 = parser.add_mutually_exclusive_group()

group_1.add_argument(
    "-v",
    "-verbose",
    action='count',
    default=0,
    help="available verbose level (1,2,3)"
    )
group_1.add_argument(
    "-q",
    "--quiet",
    action="store_true"
    )

group_2.add_argument(
    "--file",
    action="store",
    type=dir_path
    )
group_2.add_argument(
    "--folder",
    action="store",
    type=str
    )

parser.add_argument(
    "-m",
    "--mode",
    choices=["encrypt", "decrypt"],
    help="operation mode"
    )

parser.add_argument(
    "-p",
    "--password",
    help="password to app"
    )

args = parser.parse_args()
logging.getLogger().setLevel(LVL_MAPPING[args.v])

# MAIN PROGRAM
print(args)
secret = MySecret()
if args.file:
    logging.debug("FILE")
    target = "..\\result_file"
    file = args.file.split("\\")

    if os.path.exists(target):
        rmtree(target)

    os.mkdir(f'{target}')
    with open(args.file, 'r', encoding='utf-8') as file_unsafe:
        context = file_unsafe.read()
        secret.safe_context = secret.encrypt_content(context)
        logging.debug(f'Original content: {context}')
        logging.debug(f'Safe content: {secret.safe_context}')

    with open(f'{target}/{file[-1]}', 'w', encoding='utf-8') as file_safe:
        file_safe.write(secret.safe_context)

elif args.folder:
    logging.debug("FOLDER")
    target = "..\\result_folder"
    folder = args.folder.split("\\")
    if os.path.exists(target):
        rmtree(target)

    for path, directories, files in os.walk(args.folder):
        if path.startswith(".."):
            new_path = path[2:]
        os.makedirs(f'{target}/{new_path}')
        for file in files:
            with open(f'{path}/{file}', 'r', encoding='utf-8') as file_unsafe:
                context = file_unsafe.read()
                secret.safe_context = secret.encrypt_content(context)
                logging.debug(f'Original content: {context}')
                logging.debug(f'Safe content: {secret.safe_context}')

            with open(f'{target}/{new_path}/{file}', 'w', encoding='utf-8') as file_safe:
                file_safe.write(secret.safe_context)
