from datetime import datetime

with open("./change.log", "a") as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))