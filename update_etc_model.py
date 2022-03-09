#!/usr/bin/env python
"""
Update the ETC model
"""

from builtins import str
import os, sys, re, json, logging, traceback, requests, argparse, shutil
from datetime import datetime, timedelta
from requests.packages.urllib3.exceptions import (InsecureRequestWarning,
                                                  InsecurePlatformWarning)
try: from html.parser import HTMLParser
except: from html.parser import HTMLParser

# from osaka.main import get, rmall


# disable warnings for SSL verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


# set logger
log_format = "[%(asctime)s: %(levelname)s/%(funcName)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

class LogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'id'): record.id = '--'
        return True

logger = logging.getLogger('crawl_cals')
logger.setLevel(logging.INFO)
logger.addFilter(LogFilter())


def cmdLineParse():
    """Command line parser."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model_url", help="dataset version",
                        default="test", required=False)
    parser.add_argument("--tag", help="PGE docker image tag (release, version, " +
                                      "or branch) to propagate",
                        default="master", required=False)
    return parser.parse_args()


def update():
    print("Updating the model!!")
    return 0

if __name__ == '__main__':
    inps = cmdLineParse()
    try: status = update()
    except Exception as e:
        with open('_alt_error.txt', 'w') as f:
            f.write("%s\n" % str(e))
        with open('_alt_traceback.txt', 'w') as f:
            f.write("%s\n" % traceback.format_exc())
        raise
    sys.exit(status)