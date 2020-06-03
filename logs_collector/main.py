#!/usr/bin/env python3
import logging
from os.path import basename, dirname, abspath, isdir, join, isfile
import os 
import re
import itertools

base_dir = dirname(abspath(__file__))
cron_name = basename(base_dir)
cron_dir = dirname(base_dir)

logging.basicConfig(
    level=logging.INFO, 
    format=f'[%(asctime)s]:{cron_name}:%(levelname)s:%(message)s', 
    datefmt='%d-%m-%Y %H:%M:%S'
)
logging.info("Start")

# Collect all paths to info.log
log_files = []
for element in os.listdir():
    if isdir(element) and not element.startswith(".") and element != cron_name:
        log_file = join(cron_dir, element, "info.log")

        if isfile(log_file):
            log_files.append(log_file)
        else:
            logging.warning(f"{log_file} does not exist")

# Aggregate all log files
log = ""
for log_file in log_files:
    with open(log_file) as fid:
        log = log + fid.read()

log = log + "\n[03-06-2020 21:17:02]:spotify:WARNING:End"
log = log + "\n[03-06-2020 21:17:02]:spotify:ERROR:End"

# Find "expected" errors/wanings
warning_pattern = r"(.*):(.*):(WARNING):(.*)"
error_pattern = r"(.*):(.*):(ERROR):(.*)"

matches = itertools.chain(
    re.finditer(warning_pattern, log),\
    re.finditer(error_pattern, log)
)

for match in matches:
    print(":".join(match.groups()))

# Find unexpected errors

# Write all logs to a file

# Delete original logs (caution not to delete unalyzed logs)

logging.info('End')
