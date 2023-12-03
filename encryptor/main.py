import argparse
import logging
import os
import pathlib
from cryptography.fernet import InvalidToken
from crypto import Encrypt, Decrypt


def dir_path(string) -> str:
    """Check path is exists

    Args:
        string (_type_): path to check

    Raises:
        NotADirectoryError: path isn't exists

    Returns:
        str: correct patch
    """
    logging.debug('STRING: %s', string)
    if not os.path.exists(string):
        raise NotADirectoryError(string)
    return string


# INITIAL VALUES
LVL_MAPPING = {
    0: 50,  # CRITICAL
    1: 40,  # ERROR
    2: 20,  # INFO
    3: 10   # DEBUG
}

parser = argparse.ArgumentParser(description='Decrypt encrypt APP')
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
    "-f",
    "--file",
    action="store",
    type=dir_path
    )
group_2.add_argument(
    "-d",
    "--directory",
    action="store",
    type=str
    )

parser.add_argument(
    "-m",
    "--mode",
    choices=["encrypt", "decrypt"],
    type=str,
    help="operation mode"
    )

parser.add_argument(
    "-p",
    "--password",
    help="password to app"
    )

args = parser.parse_args()
logging.basicConfig(format='%(message)s')
logging.getLogger().setLevel(LVL_MAPPING[args.v])
logging.debug("Input args : %s", args)

# INIT SAMPLE FOLDERS
START_FOLDERS = ['sample_file', 'sample_folder']

for location in START_FOLDERS:
    location = '..\\' + location
    if not os.path.exists(location):
        os.mkdir(location)

# MAIN PROGRAM
try:
    # ENCRYPT
    if args.mode == "encrypt":
        logging.debug("ENCRYPT")

        # FILE / FILES
        if args.file:
            path = pathlib.Path(args.file)
            logging.debug("FILE")
            file = Encrypt(path)
            file.execute(args.password)

            logging.debug("OK")

        # DIRECTORY
        elif args.folder:
            logging.debug("DIRECTORY")
            # TODO:
            # target = "..\\result_folder"

    # DECRYPT
    elif args.mode == "decrypt":
        logging.debug("DECRYPT")

        # FILE / FILES
        if args.file:
            path = pathlib.Path(args.file)
            logging.debug("FILE")
            file = Decrypt(path)
            file.execute(args.password)

            logging.debug("OK")

        # DIRECTORY
        elif args.folder:
            logging.debug("DIRECTORY")
            # TODO:
            # target = "..\\result_folder"

except InvalidToken:
    logging.error('INVALID TOKEN')
