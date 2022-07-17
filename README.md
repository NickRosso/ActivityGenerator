


# Pre-req's
- python3 --version
- pip3 install psutil

# Set ENV vars
#### linux/Mac
- export ACTIVITY_GEN_LOG_FORMAT="CSV" //This sets the log format for each activity
- export ACTIVITY_GEN_ACTIVITY_FILE="./json_activity/linux_activity.json" //sets input activities to load
- export ACTIVITY_GEN_LOG_OUTPUT_FILE="log" //sets the output file location

#### windows
- set ACTIVITY_GEN_LOG_FORMAT=CSV
- set ACTIVITY_GEN_ACTIVITY_FILE=./json_activity/windows_activity.json
- set ACTIVITY_GEN_LOG_OUTPUT_FILE=log //sets the output file location

# How to Run
- python3 main.py

# How it works
This program runs 3 types of Activities from activity.json: Process Activity, File Activity, and Network Activity.
Every process that starts via python is logged in a log file.

- Process Activities: These are commands/files to run
- File Activity: These are commands to create, update, or delete files and log the action
- Network Activity: These are commands to start various connections to a host send data and recieve data. 


# Output

#### Windows
```
C:\Users\12243\Documents\Git\Activity_Generator>python main.py
Timed out connecting to google.com:81
Started PID's: [25076, 7496, 23816, 22436, 20324, 2216, 23648, 23156, 25276, 5540, 24772, 22024, 23676, 24684, 24684]
Start Time: 2022-07-17 10:08:30.239706 | End Time: 2022-07-17 10:08:31.415740 | Duration: 1.176034 seconds
```
#### Windows CSV Output
```
2022-07-17 10:08:30244,25076,DESKTOP-RAT2FLD\username,python3,main.py
2022-07-17 10:08:30248,7496,DESKTOP-RAT2FLD\username,chdir,
2022-07-17 10:08:30252,23816,DESKTOP-RAT2FLD\username,echo,
2022-07-17 10:08:30257,22436,DESKTOP-RAT2FLD\username,dir,
2022-07-17 10:08:30262,20324,DESKTOP-RAT2FLD\username,cmd.exe,echo > help.txt,> help.txt,Create
2022-07-17 10:08:30267,2216,DESKTOP-RAT2FLD\username,cmd.exe,echo > test.png,> test.png,Create
2022-07-17 10:08:30272,23648,DESKTOP-RAT2FLD\username,cmd.exe,echo > help.csv,> help.csv,Create
2022-07-17 10:08:30277,23156,DESKTOP-RAT2FLD\username,cmd.exe,echo > help.txt,> help.txt,Update
2022-07-17 10:08:30282,25276,DESKTOP-RAT2FLD\username,cmd.exe,echo > test.png,> test.png,Update
2022-07-17 10:08:30286,5540,DESKTOP-RAT2FLD\username,cmd.exe,echo > help.csv,> help.csv,Update
2022-07-17 10:08:30291,24772,DESKTOP-RAT2FLD\username,cmd.exe,del /f help.txt,/f help.txt,Delete
2022-07-17 10:08:30295,22024,DESKTOP-RAT2FLD\username,cmd.exe,del /f test.png,/f test.png,Delete
2022-07-17 10:08:30300,23676,DESKTOP-RAT2FLD\username,cmd.exe,del /fhelp.csv,/fhelp.csv,Delete
2022-07-17 10:08:30415,24684,DESKTOP-RAT2FLD\username,python.exe,142.250.190.110,80 192.168.1.21,65476,18,54497
2022-07-17 10:08:31415,24684,DESKTOP-RAT2FLD\username,python.exe,google.com,81 0.0.0.0,0,0,0
```
## Linux
```
username@DESKTOP-RAT2FLD:/mnt/c/Users/12243/Documents/Git/Activity_Generator$ python3 main.py
Timed out connecting to google.com:81
Started PID's: [2828, 2830, 2831, 2833, 2835, 2837, 2839, 2841, 2843, 2845, 2847, 2849, 2851, 2827, 2827]
Start Time: 2022-07-17 10:08:25.867275 | End Time: 2022-07-17 10:08:27.000374 | Duration: 1.133099 seconds
```

### Linux CSV Output
```
2022-07-17 10:08:25870,2828,username,python3,main.py --help --too
2022-07-17 10:08:25871,2830,username,pwd,--help
2022-07-17 10:08:25872,2831,username,./test_executables/hello_world.sh,
2022-07-17 10:08:25874,2833,username,ls,
2022-07-17 10:08:25875,2835,username,sh,touch help.txt,help.txt,Create
2022-07-17 10:08:25876,2837,username,sh,touch test.png,test.png,Create
2022-07-17 10:08:25878,2839,username,sh,touch help.csv,help.csv,Create
2022-07-17 10:08:25879,2841,username,sh,touch help.txt,help.txt,Update
2022-07-17 10:08:25880,2843,username,sh,touch test.png,test.png,Update
2022-07-17 10:08:25881,2845,username,sh,touch help.csv,help.csv,Update
2022-07-17 10:08:25883,2847,username,sh,rm help.txt,help.txt,Delete
2022-07-17 10:08:25884,2849,username,sh,rm test.png,test.png,Delete
2022-07-17 10:08:25885,2851,username,sh,rm help.csv,help.csv,Delete
2022-07-17 10:08:25997,2827,username,python3,142.250.190.110,80 172.30.18.233,43438,18,54494
2022-07-17 10:08:26999,2827,username,python3,google.com,81 0.0.0.0,0,0,0
```
# Troubleshooting
- If you see expected str, bytes or os.PathLike object, not NoneType this means you need to set your environment variables to run the generator.


# Known issues
- Full file paths for processes/file/activity will only be logged if activity.json contains full file paths.
- Each Network Activity will share a PID i.e. each Network activity call does not start a new PID since it is running within python and not the OS's CLI