import os
import psutil
import sqlite.py

safeList = []
unsafeList = []
currentProcessesName = []
currentPID = []


def processesRunning():
    # # Running the aforementioned command and saving its output
    # output = os.popen('wmic process get description, processid').read()

    # # Displaying the output
    # # print(output)

    # # Add to process list
    # currentProcesses.append(output)

    processCount = 0

    for process in psutil.process_iter():
        processCount += 1
        name = process.name()  # Name of the process
        ID = process.pid  # ID of the process
        currentProcessesName.append(name)
        currentPID.append(ID)
    print("\nTotal number of running process are ", processCount)

processesRunning()


def safe(processList):
    for x in processList:
        userInput = input("Is {} safe? (Y/N): ".format(x))
        if userInput == "Y" or userInput == "y":
            safeList.append(x)
        else:
            if userInput == "N" or userInput == "n":
                unsafeList.append(x)
                print("WARNING! ", x, " IS NOT SAFE!")
            else:
                print("INVALID INPUT. TRY AGAIN")
                x = x-1



safe(currentProcessesName)
