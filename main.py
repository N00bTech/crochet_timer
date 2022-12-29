from time import sleep
from os import listdir, system
import csv


def create_file():
    try:
        user_filename = str(input("Project Name: "))
        with open(f'projects/{user_filename}.csv', 'a') as project:
            fieldnames = ['Hours', 'Minutes', 'Seconds', 'Earned']
            writer = csv.DictWriter(project, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Hours': 0, 'Minutes': 0, 'Seconds': 0, 'Earned': 0.0})
    except KeyboardInterrupt:
        print("Exit...")

def open_file():
    try:
        files = listdir("projects")
        print("========================================================")
        print("Available Projects: ")
        for file in files:
            print(file[:-4])
        print("========================================================")
        user_open_filename = str(input("Project: "))
        COST_PER_MINUTE = .50
        FIELDNAMES = ['Hours', 'Minutes', 'Seconds', 'Earned'] 
        system('cls')
        while True:
            with open(f'projects/{user_open_filename}.csv', 'r') as project:
                READER = csv.DictReader(project)
                for row in READER:
                    hours = int(row['Hours'])
                    minutes = int(row['Minutes'])
                    seconds = int(row['Seconds'])
                    earned = float(row['Earned'])
                print(f"{hours} Hours - {minutes} Minutes - {seconds} Seconds |-|-| {earned} Pesos", end="\r")

            with open(f'projects/{user_open_filename}.csv', 'a') as project:
                WRITER = csv.DictWriter(project, fieldnames=FIELDNAMES)
                sleep(1)
                seconds += 1
                if seconds == 61:
                    minutes += 1
                    seconds = 1
                    earned += COST_PER_MINUTE
                elif minutes == 61:
                    hours += 1
                    minutes = 0
                WRITER.writerow({'Hours': hours, 'Minutes': minutes, 'Seconds': seconds, 'Earned': earned})
    except KeyboardInterrupt:
        print("\n\nExit...")

if __name__ == "__main__":
    print("""  _____             __       __    _______              
 / ___/______  ____/ /  ___ / /_  /_  __(_)_ _  ___ ____
/ /__/ __/ _ \/ __/ _ \/ -_) __/   / / / /  ' \/ -_) __/
\___/_/  \___/\__/_//_/\__/\__/   /_/ /_/_/_/_/\__/_/
========================================================
1. Create New File
2. Open File
========================================================""")
    user_choice = int(input("Input Choice: "))
    while True:
        if user_choice == 1:
            create_file()
            break
        elif user_choice == 2:
            open_file()
            break
        else:
            user_choice = int(input("Input Choice: "))
            continue
