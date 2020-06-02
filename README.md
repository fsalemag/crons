# Raspberry Pi cron jobs



### Structure
One folder per cron job
Submodules should be added in helper/, this folder is included in the crons path so it is accessible to any cron job 


### Adding a new cron job
crontab -e 


### Crontabs 
Register of current system crons


### Connect to bluetooth speaker and start playing generated playlist 
`* * * * * ~/crons/spotify/main.py >> ~/cros/spotify/info.log 2>> ~/cros/spotify/errors.log `

### Collect all the error logs and join them 
`0 0 * * * ~/crons/logs/main.py >> ~/cros/logs/info.log 2>> ~/cros/logs/errors.log `


### TODO
- Logging module to include timestamps
- Error collection

