#!/usr/bin/env python3
''' Cron intended to check if there is a connection via bluetooth with any device.
If there is a connection:
  Launches tizonia, a music terminal streaming service.
  Generates a spotify playlist and plays it
If there is no connection, guarantee there is no tizonia running.
'''

import logging
import subprocess
import os 
import playlist_generator
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

connect_bluetooth = subprocess.run(f"{base_dir}/connect_bluetooth.sh", shell=True, capture_output=True, text=True)

if "info Missing device" in connect_bluetooth.stdout:
    logging.log("No device available")

    # Kill every instance of tizonia in case it exists
    subprocess.Popen("ps aux | grep tizonia | awk '{print $2}' | xargs kill", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
else:
    logging.info('Connected')
    
    # os.system(f'{base_dir}/start_stream.sh')
    stream = subprocess.run(f'{base_dir}/start_stream.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   
    # Only updates playlist when "stream" finished (when we get the actual output of the script)
    # This way if we like a song we can check the playlist and ensure it is the one being played
    if "update" in stream.stdout:
        logging.info("Generate playlist")
        sp = playlist_generator.Spotify()
        sp.update_playlist("Auto generated")
    else:
        logging.info("No playlist generated")

logging.info('End')
