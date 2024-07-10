import argparse
from colorama import Fore, Style, init
from impacket import smb, smb3, nmb, nt_errors, LOG
import socket
import urllib3
import os
from os.path import exists
import datetime
import textwrap
import sys
import getpass


global domain


def options():
    opt_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example: python3 smb_scanner.py tool -t 192.168.1.1"""
        ),
    )
    requiredNamed = opt_parser.add_argument_group("required arguments")
    requiredNamed.add_argument(
        "-t", "--target", help="Specifies the ip address of the target.", required=True
    )
    global args
    args = opt_parser.parse_args()
    if len(sys.argv) == 1:
        opt_parser.print_help()
        opt_parser.exit()
    global success, info, fail
    success, info, fail = (
        Fore.GREEN + Style.BRIGHT,
        Fore.YELLOW + Style.BRIGHT,
        Fore.RED + Style.BRIGHT,
    )


def get_os_type():
    if sys.platform.startswith("win32"):
        getpass.getuser()
    elif sys.platform.startswith("dariwn"):
        pass
    elif sys.platform.startswith("linux"):
        pass
