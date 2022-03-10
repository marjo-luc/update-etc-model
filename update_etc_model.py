#!/usr/bin/env python
"""

PGE that calls the performance estimator's 'update' endpoint
to update the performance estimator's model.

See: https://github.jpl.nasa.gov/kpearson/SOAMC-job-etc

"""

from builtins import str
import os, sys, re, json, logging, traceback, requests, argparse, shutil
from datetime import datetime, timedelta
from requests.packages.urllib3.exceptions import (InsecureRequestWarning,
                                                  InsecurePlatformWarning)
try: from html.parser import HTMLParser
except: from html.parser import HTMLParser

from osaka.main import get, rmall


# disable warnings for SSL verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


# Set up SDSWatch Logger for fulldict
host = "factotum"
source_type = "performance_estimator"
source_id = "pge"

log_format = ("\'%(asctime)s.%(msecs)03d\',"
                      "\'" + host + "\',"
                      "\'" + source_type + "\',"
                      "\'" + source_id + "\',"
                      "%(params)s")
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(log_format, datefmt=datefmt)
level = logging.INFO

sdswatch_handler = logging.FileHandler(filename = 'performance_estimator.fulldict.sdswatch.log')
sdswatch_handler.setLevel(level)
sdswatch_handler.setFormatter(formatter)

logger = logging.getLogger("sdswatch")
logger.setLevel(level)
logger.addHandler(sdswatch_handler)
logging.Formatter.converter = time.gmtime


class LogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'id'): record.id = '--'
        return True

# logger = logging.getLogger('performance_estimator.sdswatch.log')
# logger.setLevel(logging.INFO)
# logger.addFilter(LogFilter())


def cmdLineParse():
    """Command line parser"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model_url", help="url to performance estimator model", default="jobs.db", required=False)
    parser.add_argument("--host", help="host running performance estimator service", default="http://localhost:5000", required=False)
    return parser.parse_args()


def update(host, model_url):
    print("Updating the model!!")
    url = host + '/update'
    print(url)
    r = requests.get(url)
    sdsw_logger.log(status_code=r.status_code)
    print(r)
    return 0


def push_model_to_cloud():
    # push the job.db model that's located locally to s3
    return 0

if __name__ == '__main__':
    inps = cmdLineParse()
    try: 
        status = update(inps.host, inps.model_url)
    except Exception as e:
        with open('_alt_error.txt', 'w') as f:
            f.write("%s\n" % str(e))
        with open('_alt_traceback.txt', 'w') as f:
            f.write("%s\n" % traceback.format_exc())
        raise
    sys.exit(status)