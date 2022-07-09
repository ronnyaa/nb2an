#!/usr/bin/python3

"""List attributes of a device"""

import requests
import nb2an.netbox

try:
    from rich import print
except Exception:
    pass

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from logging import debug, info, warning, error, critical
import logging
import sys
import yaml


def parse_args():
    "Parse the command line arguments."
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            description=__doc__,
                            epilog="Exmaple Usage: ")

    parser.add_argument("-b", "--blanks", action="store_true",
                        help="Show blank areas with blank lines")

    parser.add_argument("--log-level", "--ll", default="info",
                        help="Define the logging verbosity level (debug, info, warning, error, fotal, critical).")

    parser.add_argument("devices", type=str, nargs="*", default=None,
                        help="Device number")

    args = parser.parse_args()
    log_level = args.log_level.upper()
    logging.basicConfig(level=log_level,
                        format="%(levelname)-10s:\t%(message)s")
    return args


def main():
    args = parse_args()

    for device in args.devices:
        try:
            debug(f"trying by id: {device}")
            id = int(device)
            device = nb2an.netbox.Netbox().get_devices_by_id(id)
        except Exception:
            debug(f"trying by name: {device}")
            device = nb2an.netbox.Netbox().get_devices_by_name(device)
        
        print(yaml.dump(device))

if __name__ == "__main__":
    main()


