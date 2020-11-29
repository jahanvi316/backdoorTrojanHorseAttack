import os
import psutil
import database

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


def safe(processNameList, processPIDList):
    for name, pid in zip(processNameList, processPIDList):
        userInput = input("Is {} safe? (Y/N): ".format(name))
        if userInput == "Y" or userInput == "y":
            database.addProcess(pid, name, 1)
        else:
            if userInput == "N" or userInput == "n":
                database.addProcess(pid, name, 0)
                print("WARNING! ", name, " IS NOT SAFE!")
            else:
                print("INVALID INPUT. TRY AGAIN")



safe(currentProcessesName, currentPID)

