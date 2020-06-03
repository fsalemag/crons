Raspberry Pi cron jobs
==============


Structure
---------
One folder per cron job.

Submodules should be added in `helper/`, this folder is included in the crons path so it is accessible to any cron job.


Current crons
-------------
* Connect to bluetooth speaker and start playing auto generated playlist (every minute between 9am and 1am)
* Collect all the error/warning logs and join them (daily at midnight)

Cron file
---------
    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:~/crons/helper

    * 9-23,0-1 * * * ~/crons/spotify/main.py >> ~/crons/spotify/info.log 2>&1

    0 0 * * * ~/crons/spotify/main.py >> ~/crons/spotify/info.log 2>&1

TODO
----
- Email CLI tool

