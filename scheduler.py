import os, subprocess
import urllib.request
from distutils.version import StrictVersion
import re
import sched, time

def isProcessRunning(procname):
    def getTasks(name):
        r = os.popen('tasklist').read().strip().split('\n')
        #print ('# of tasks is %s' % (len(r)))
        for i in range(len(r)):
            s = r[i]
            if name in r[i]:
                #print ('%s in r[i]' %(name))
                return r[i]
        return []
    return getTasks(procname) != []

def killProcess(procname):
    try:
        os.system("taskkill /im " + procname)
        return True
    except Exception as e:
        return False

def startProcess(pdir):
    try:
        if pdir.endswith(".py"):
            os.system('python ' + pdir)
        else:
            os.startfile(pdir)
        return True
    except (Exception) as e:
        return False

def checkForUpdate(url, verreg, version):
    print("WIP Function")
    try:
        urldata = urllib.request.urlopen(updateurl).read().decode("utf-8", "ignore")
        m = re.search(verreg, urldata)
        v = m.group(1)
        print(v)
        if StrictVersion(v) > StrictVersion(v):
            return True
    except Exception as e:
        print("An error has occured with check for update.")
    return False

def scheduledTask(function, delay, priority=1):
    """
    function - function which runs after the delay. This function should not take args.
    delay - the delay between when the function will be ran (in seconds)
    priority - the priority of the task
    """
    def getDelay():
        if type(delay) == type([]):
            if len(delay) > 0:
                d = delay.pop()
                if d < 0:
                    raise ValueError("All delays must be positive values!")
                return d
            else:
                print("Exiting scheduler...")
                return False
        elif type(delay) == type(0):
            return delay
        else:
            raise ValueError("The delay was not of type int or list!")
    
    def routine():
        if (function()):
            d = getDelay()
            if d is not False:
                print("Waiting for " + str(d) + " second(s)...\n")
                s.enter(d, priority, routine)
    
    
    s = sched.scheduler(time.time, time.sleep)
    routine()
    s.run()