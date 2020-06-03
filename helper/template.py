#!/usr/bin/env python3
import logging
from os.path import basename, dirname, abspath

base_dir = dirname(abspath(__file__))
cron_name = basename(base_dir)

logging.basicConfig(
    level=logging.INFO, 
    format=f'[%(asctime)s]:{cron_name}:%(levelname)s:%(message)s', 
    datefmt='%d-%m-%Y %H:%M:%S'
)

logging.info('Start')

logging.info('End')
