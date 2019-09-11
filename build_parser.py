# Given a folder of build files that might look like this:

# /Build-1.dmg
# /Build-2.dmg
# /Build-2.1.dmg
# /Build-2.1.1.dmg
# /Build-3.dmg
# /Build-3.3.dmg
# /Build-3.19.dmg

# Write a script that takes a path to the folder as an argument, and prints the highest build number (just the number, i.e. 2.1.1)
# Note:  The first digit can go up to 999 and should always be present, but the second and third can only go up to 99, and might not be included.

import os

def highestBuildNumber(pathToFolder):
    fileList = os.listdir(pathToFolder)
    xList = list(dict.fromkeys(map(lambda y: y.split("Build-")[1].split(".dmg")[0],fileList)))
    i = 0
    while (True):
        xList = list(filter(lambda x: len(x.split(".")) > i, xList))
        myMax = max(xList, key=lambda m: int(m.split(".")[i]))
        xList = list(filter(lambda x: x.split(".")[i] == myMax.split(".")[i], xList))
        
        if len(xList) == 1:
            print (xList[0])
            break
        else:
            i += 1
    
    return xList[0]


highestBuildNumber("build_tests")