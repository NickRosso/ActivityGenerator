from classes.FileActivity import FileActivity
from classes.ProcessActivity import ProcessActivity
from classes.NetworkActivity import NetworkActivity
import json

if __name__ == "__main__":
    log_format = "CSV"
    f = open("activity.json")
    data = json.load(f)
    for process in data['ProcessActivity']:
        ProcessActivity(command=process['command'], commandOptions=process['commandOptions'], logFormat=log_format)

    for process in data['FileActivity']:
         FileActivity(command=process['command'], commandOptions=process['commandOptions'], logFormat=log_format, action=process['action'])

    for process in data['NetworkActivity']:
        NetworkActivity(dest_hostname=process["dest_hostname"], dest_port=process["dest_port"], protocol=process["protocol"], data=process["data"], logFormat=log_format)