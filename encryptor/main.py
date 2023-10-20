import argparse


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

group_2.add_argument("--file", action="store_true")
group_2.add_argument("--folder", action="store_true")

parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="operation mode")
parser.add_argument("-p", "--password", help="password to app")

args = parser.parse_args()
print(args)