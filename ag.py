import sys
sys.path.insert(0, "ThaumTechLib")
from timeout import timeout
#This is just an example test file.
from time import sleep

@timeout(5)
def F(n):
    sleep(n)


F(35)