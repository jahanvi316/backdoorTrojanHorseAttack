import psutil, sys
from subprocess import Popen


def findProcess(processName):
    print("findProcess running for ", processName)
    try:
        for process in psutil.process_iter():
            if process.cmdline() == ['python', processName]:
                sys.exit('Process found: exiting.')

        print('Process not found: not running.')
    except ValueError:
        print("An error occurred:")
        print(ValueError)


process = sys.argv[1]
findProcess(process)