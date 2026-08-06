from datetime import datetime

def write_log(option):

    with open("outputs/log.txt", "a") as file:

        current_time = datetime.now()

        file.write(f"{current_time} - {option}\n")