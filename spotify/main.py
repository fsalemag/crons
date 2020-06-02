#!/usr/bin/env python3
''' Cron intended to check if there is a connection via bluetooth with any device.
If there is a connection:
  Launches tizonia, a music terminal streaming service.
  Generates a spotify playlist and plays it
If there is no connection, guarantee there is no tizonia running.
'''

import subprocess
import os 
import playlist_generator

base_dir = os.path.dirname(os.path.realpath(__file__))

connect_bluetooth = subprocess.run(f"{base_dir}/connect_bluetooth.sh", shell=True, capture_output=True, text=True)

if "info Missing device" in connect_bluetooth.stdout:
    print("No device available")

    # Kill every instance of tizonia in case it exists
    subprocess.Popen("ps aux | grep tizonia | awk '{print $2}' | xargs kill", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
else:
    print("Connected")
    sp = playlist_generator.Spotify()
    sp.update_playlist("Auto generated")
    os.system(f'{base_dir}/start_stream.sh')
