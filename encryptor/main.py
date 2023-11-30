import argparse
import logging
import os
from secret import MySecret


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


START_FOLDERS = ['sample_file', 'sample_folder']

for location in START_FOLDERS:
    location = '..\\' + location
    if not os.path.exists(location):
        os.mkdir(location)

secret = MySecret()

# MAIN PROGRAM
if args.mode == "encrypt":
    logging.debug("ENCRYPT")
    if args.file:
        logging.debug("FILE")

        target = "..\\result_file"
        secret.encrypt_file(args, target)

    elif args.folder:
        logging.debug("FOLDER")
        target = "..\\result_folder"
        secret.encrypt_folder(args, target)

elif args.mode == "decrypt":
    logging.debug("DECRYPT")
