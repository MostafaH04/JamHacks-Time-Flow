from io import BufferedReader
import psutil
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app
from firebase_admin import db
from signin import signup
from reference import reference

unwantedDelay = 60 * 60
deduct = False

def checkUnwanted(currTimeUnwanted):
    if time.time() - currTimeUnwanted > unwantedDelay:
        return True
    pass


ref = db.reference("/Users")
ref2 = db.reference("/bad")
ref3 = db.reference("/good")

goodApps = ref3.get()
badApps = ref2.get()

openApps = []
unwantedAppsOpen = []
preferredOpen = []

unwatnedNum = 0
wantedNum = 0

logged = False

file2 = open(r"logged.txt","r")
lines = file2.readlines()
if 'False' in lines[0]:
    logged = False
else:
    logged = True
file2.close()

if logged == True:
    file = open(r"scores.txt", "r")
    lines = file.readlines()
    user, points = lines[0].split()
    file.close()
    points = float(points)

pointsPositive = 3
pointsNegative = -1
pointsUnwanted = -0.5

posPerApp = 0.01
negPerApp = 0.005

unWanted = False
wanted = False
unHealthy = False

currTime = time.time()
currTimeUnwanted = time.time()
timeDelay = 60


while True:
    file2 = open(r"logged.txt","r")
    lines = file2.readlines()
    if lines[0] == 'False':
        logged = False
    else:
        logged = True
    file2.close()

    if logged == True:
        users = ref.get()
        print(len(users))
        userPos = None
        print(users)
        keyList = []
        for key in users.keys():
            keyList.append(key)
        print(keyList)
        for userNum in range(len(users)):
            if user == users[keyList[userNum]]['username']:
                ref.child(keyList[userNum]).update({"points": points})

        file = open(r"scores.txt", "w+")
        strOut = f"{user} {points}"
        if file.read != strOut:
            file.write(strOut)
        file.close()

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

                for i in badApps:
                    if i in stuff.lower():
                        unwantedAppsOpen.append(stuff)
                for i in goodApps:
                    if i in stuff.lower():
                        preferredOpen.append(stuff)

            for stuff in temp2:
                print(stuff + " out") 
                openApps.pop(openApps.index(stuff))
                if stuff in unwantedAppsOpen:
                    unwantedAppsOpen.pop(unwantedAppsOpen.index(stuff))
                elif stuff in preferredOpen:
                    preferredOpen.pop(preferredOpen.index(stuff))
        
        unwantedNum, wantedNum = len(unwantedAppsOpen), len(preferredOpen)
        print(f"\n\nUnwanted: {unwantedNum}-{unwantedAppsOpen}\nWanted: {wantedNum}-{preferredOpen}")

        if unwantedNum > 0:
            unWanted = True
        else: unWanted = False

        if wantedNum > 0:
            wanted = True
        else: wanted = False



        if time.time() - currTime > timeDelay:
            if wanted == True:
                points += pointsPositive + ((0.01) * wantedNum)
            
            if unWanted == True:
                deduct = checkUnwanted(currTimeUnwanted)
                if deduct:
                    points += pointsNegative - ((0.005) * unwantedNum) 
            else:
                currTimeUnwanted = time.time()

            if unHealthy == True:
                points += pointsUnwanted
            
            currTime = time.time()

            print(points)
    else:
        signup()
        file = open(r"scores.txt", "r")
        lines = file.readlines()
        user, points = lines[0].split()
        file.close()
        points = float(points)
    


    

    