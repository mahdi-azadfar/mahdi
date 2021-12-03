# this program will produce a random password with specific options
import random
import string
import argparse


def password_creator(
        length, upper=False, lower=False, digit=False, pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == '':
        pool += string.ascii_letters
    if length is None:
        length = 8
    return ''.join(random.choices(pool, k=length))


parser = argparse.ArgumentParser(description='PASSWORD CREATOR')
parser.add_argument('--length', type=int, help='Length of password')
parser.add_argument('--upper', action="store_true", help='use upper case in password')
parser.add_argument('--lower', action="store_true", help='use lower case in password')
parser.add_argument('--digit', action="store_true", help='use digit in password')
parser.add_argument('--pun', action="store_true", help='use punctuation in password')
args = parser.parse_args()
print(f'\nPASSWORD: {password_creator(args.length, args.upper, args.lower, args.digit, args.pun)}\n')
