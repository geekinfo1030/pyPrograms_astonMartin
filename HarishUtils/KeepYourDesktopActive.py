import pyautogui as pyg
import time
import requests
import sys

pyg.PAUSE = 1
pyg.FAILSAFE = True

width, height = pyg.size()

"""print('width'+width  'height= '+ height)"""


def DoSomeRandom():
    for i in range(1):
        pyg.moveTo(1400, 2000, duration=0.25)
        print('DoSomeRandom')
        #
        pyg.moveTo(1200, 2000, duration=0.25)
        pyg.moveTo(1400, 2000, duration=0.25)
        pyg.moveTo(1200, 2000, duration=0.25)


def DoSomeRandomForIndiniteTime():
    while (True):
        # pyg.moveTo(1400,2000,duration=0.25)
        pyg.click(1400, 2000)
        print('DoSomeRandom')
        time.sleep(5)
        pyg.FAILSAFE = False
        pyg.click(1200, 2000)


def DoSomeRandom1():
    for i in range(10):
        print('DoSomeRandom1')
        pyg.moveRel(100, 0, duration=0.25)
        time.sleep(2000)
        pyg.moveRel(0, 100, duration=0.25)
        pyg.moveRel(-100, 0, duration=0.25)
        pyg.moveRel(0, -100, duration=0.25)


def GetMountPointerLocation():
    x, y = pyg.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)


def DoMouseClick(x, y):
    pyg.click(x, y)


teamsXWith = 715
teamsYHeight = 1069
skypeXWidth = 767
skypeYwidth = 1069


def matchCoordinateAgainstPixel(xcor, ycor, r, g, b):
    return pyg.pixelMatchesColor(xcor, ycor, (r, g, b))


def mainEntryPoint():
    print('press ctrc-c to quit.')
    try:
        i = 0
        while (i < 5):
            print('Do one app click ')
            print(i)

            ###sys.stdout.write(teamsXWith)

            DoMouseClick(teamsXWith, teamsXWith)
            time.sleep(20)
            print('Second click ')
            DoMouseClick(skypeXWidth, skypeYwidth)
            i = i + 1

    except KeyboardInterrupt:
        print('\n Done')


def readFromCSV():
    with open('bussers.csv') as data:
        ignore = data.readline()
        flights = {}
        for line in data:
            k, v = line.strip().split(',')
            flights[k] = v


def GetResponse(urls):
    for resp in (requests.get(url) for url in urls):
        print(len(resp.content), '->', resp.status_code, '->', resp.url)


# mainEntryPoint()

DoSomeRandomForIndiniteTime()





