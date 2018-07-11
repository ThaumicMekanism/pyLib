import scheduler

pname = "file.exe"
pdir = "run.bat"
def fn():
    print("running")
    if (not scheduler.isProcessRunning(pname)):
        print("Process is not running! Starting it...")
        #scheduler.startProcess(pdir)
    #print(scheduler.checkForUpdate())
    return True


#scheduler.scheduledTask(fn, 5)

def ag():
	print("Testing...")

	#Use the & to run the process in the background. Works for linux and windows does not care
	#You could also start your process however you want to as well.
	scheduler.startProcess("ag.py &")

	print("Finished testing...")
	return True
#This delay is in seconds. Goes from right to left. Scheduler also starts off runing the process first, then waiting.

scheduler.scheduledTask(ag, [3600*10, 3600*14, 3600*10, 3600*14, 3600*5, 3600*5, 3600*11, 3600*3])