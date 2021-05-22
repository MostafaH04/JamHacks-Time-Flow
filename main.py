import psutil
import time

badApps = ["valorant.exe" , "RocketLeague.exe"]


openApps = []
unwantedAppsOpen = []

points = 0

pointsPositive = 3
pointsNegative = -1
pointsUnwanted = -0.5

def unwanted():
    return False


while True:

    # Checks which applications just opened or closed and adds / removes them from the open Apps list
    currOpen = []
    for apps in psutil.process_iter():
        currOpen.append(apps.name())
    if currOpen != openApps:
        temp1 = set(currOpen).difference(set(openApps))
        temp2 = set(openApps).difference(set(currOpen))
        for stuff in temp1:
            print(stuff + " in")
            openApps.append(stuff)
        for stuff in temp2:
            print(stuff + " out") 
            openApps.pop(openApps.index(stuff))
    



    
    


    

    

    