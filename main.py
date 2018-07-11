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

	scheduler.startProcess("ag.py")

	print("Finished testing...")
	return True
#This delay is in seconds. Goes from right to left
scheduler.scheduledTask(ag, [3600*6])