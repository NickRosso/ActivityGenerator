import os
import sys
import json
import datetime
from classes.FileActivity import FileActivity
from classes.ProcessActivity import ProcessActivity
from classes.NetworkActivity import NetworkActivity

if __name__ == "__main__":
    try:
        log_format = os.environ.get("ACTIVITY_GEN_LOG_FORMAT")
        activity_file = open(os.environ.get("ACTIVITY_GEN_ACTIVITY_FILE"))
        activity_json = json.load(activity_file)

    except Exception as e:
        print(e)
        exit(1)

    #cant forget Logging activity of current process
    start_time = datetime.datetime.now()
    PIDs_started = []
    activity = ProcessActivity(command="python3", commandOptions=" ".join(sys.argv), logFormat=log_format)
    PIDs_started.append(activity.processID)
    #loading processes to run from ProcessActivity JSON array in 
    for process in activity_json['ProcessActivity']:
        activity = ProcessActivity(command=process['command'], commandOptions=process['commandOptions'], logFormat=log_format)
        PIDs_started.append(activity.processID)

    for process in activity_json['FileActivity']:
        activity = FileActivity(command=process['command'], commandOptions=process['commandOptions'], logFormat=log_format, action=process['action'])
        PIDs_started.append(activity.processID)

    for process in activity_json['NetworkActivity']:
        activity = NetworkActivity(dest_hostname=process["dest_hostname"], dest_port=process["dest_port"], protocol=process["protocol"], data=process["data"], logFormat=log_format)
        PIDs_started.append(activity.processID)

    end_time = datetime.datetime.now()
    print(f"Started PID's: {PIDs_started}")
    print(f"Start Time: {start_time} | End Time: {end_time} | Duration: {(end_time - start_time).total_seconds()} seconds")