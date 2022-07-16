from classes.FileActivity import FileActivity
from classes.ProcessActivity import ProcessActivity

if __name__ == "__main__":
    log_format = "CSV"
    file_creation_command = "touch"
    file_deletion_command = "rm"
    process_path = '/mnt/c/Users/12243/Documents/Git/Activity_Generator/'

    ProcessActivity(command='pwd', commandOptions="--help", logFormat=log_format)
    ProcessActivity(command='pwd', commandOptions="--help", logFormat=log_format)
    ProcessActivity(command="./test_executables/hello_world.sh", logFormat=log_format)
    ProcessActivity(command="ls", commandOptions="--name", logFormat=log_format)
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}help.txt", logFormat=log_format, action="Create")
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}test.png", logFormat=log_format, action="Create")
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}test.csv", logFormat=log_format, action="Create")
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}help.txt", logFormat=log_format, action="Update")
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}test.png", logFormat=log_format, action="Update")
    FileActivity(command=file_creation_command, commandOptions=f"{process_path}test.csv", logFormat=log_format, action="Update")
    FileActivity(command=file_deletion_command, commandOptions=f"{process_path}help.txt", logFormat=log_format, action="Delete")
    FileActivity(command=file_deletion_command, commandOptions=f"{process_path}test.png", logFormat=log_format, action="Delete")
    FileActivity(command=file_deletion_command, commandOptions=f"{process_path}test.csv", logFormat=log_format, action="Delete")
