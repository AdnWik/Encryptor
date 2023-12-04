import argparse
import logging
import os
import pathlib
from time import time
from tqdm import tqdm
from cryptography.fernet import InvalidToken
from crypto import Encrypt, Decrypt


def main(args):
    # MAIN PROGRAM
    start = time()
    try:
        # FILE / FILES
        if args.file:

            files_to_process = args.file
            if args.verbose == 3:
                files_to_process = tqdm(args.file)
            for file in files_to_process:
                file = pathlib.Path(file)

                if args.mode == "encrypt":
                    action = Encrypt(file)
                elif args.mode == "decrypt":
                    action = Decrypt(file)

                action.execute(args.password)
                stop = time()
                process_time = stop - start
                verbose(file, process_time, files_to_process)

        # DIRECTORY
        elif args.folder:
            # TODO:
            pass

    except InvalidToken:
        print("INVALID TOKEN")


def verbose(file, process_time, files_to_process):
    # VERBOSE
    if args.verbose == 1 or args.verbose <= 2:
        # VERBOSE LEVEL 1
        print(f'File: {file.name}', end='')

        if args.verbose == 2:
            # VERBOSE LEVEL 2
            print(f' Processed in: {process_time} sec', end='')

        print()

    if args.verbose >= 3:
        # VERBOSE LEVEL 3
        files_to_process.set_description(file.name)


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


# INIT SAMPLE FOLDERS
START_FOLDERS = ['sample_file', 'sample_folder']

for location in START_FOLDERS:
    location = '..\\' + location
    if not os.path.exists(location):
        os.mkdir(location)

# INIT DATA FROM CONSOLE
parser = argparse.ArgumentParser(description='Decrypt encrypt APP')
group_1 = parser.add_mutually_exclusive_group()
group_2 = parser.add_mutually_exclusive_group()

group_1.add_argument(
    "-v",
    "--verbose",
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
    action="append",
    type=str
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

main(args)
