import argparse
from os import getenv
from dotenv import load_dotenv
import logging
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


load_dotenv()
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
    action="store_true"
    )
group_2.add_argument(
    "--folder",
    action="store_true"
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
print(args)

LVL_MAPPING = {
    0: 50,  # CRITICAL
    1: 40,  # ERROR
    2: 20,  # INFO
    3: 10   # DEBUG
}

logging.getLogger().setLevel(LVL_MAPPING[args.v])

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=getenv('SALT').encode('utf-8'),
    iterations=480000
    )


token = Fernet(
    base64.urlsafe_b64encode(kdf.derive(getenv('PASSWORD').encode('utf-8')))
    )

text = input('>>> ')

safe_text = token.encrypt(text.encode('utf-8'))
logging.info(safe_text)

decoded_text = token.decrypt(safe_text).decode('utf-8')
print(decoded_text)
