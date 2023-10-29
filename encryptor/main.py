import argparse
import logging
from os import getcwd
import pathlib
from my_secret import MySecret

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
    type=str
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
    print(getcwd()+"\\"+args.file)

else:
    logging.debug("FOLDER")
