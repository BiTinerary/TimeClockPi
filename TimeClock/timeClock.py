import OPi.GPIO as GPIO
from blinky import *
from gSheetPunch import *
from threading import Thread
import datetime, time, sys, os

dirname = os.path.split(os.path.abspath(__file__))[0]

def threadFunction(func, array):
        return Thread(target=func, args=(array))

def MasterLog(directory, employee, data):
        with open('%s/%s/MasterTimeClockLog.csv' % (dirname, directory), 'a+') as MasterLog:
                MasterLog.write("%s,%s" % (employee, data))
        MasterLog.close()
        print 'Master Log Written Succesfully!'
        blink(['red', 'green'], 3)

def timeCard(punch):
        worksheet, employee, data, action = punch[0], punch[1], punch[2], punch[3]
        directory = 'TimeCards'
        
        if not os.path.exists("%s/%s" % (dirname, directory)):
                os.makedirs("%s/%s" % (dirname, directory))
                
        with open("%s/%s/%s.csv" % (dirname, directory, employee), 'a+') as employeeLogFile:
                timeCardData = "%s,%s,%s\n" % (action, data[0], data[1])
                employeeLogFile.write(timeCardData)
        employeeLogFile.close()

        MasterLogThread = threadFunction(MasterLog, [directory, employee, timeCardData]) ## GOOGLE API CREDZ PARAM
        MasterLogThread.start()
        
        try:
                gSheetThread = threadFunction(gSheetPunch, [worksheet, employee, action])
                gSheetThread.start()
        except:
                blink(redLedPin, 10)
        print "%s %s on %s at %s" % (employee, action, data[0], data[1])


def mainSwipe(worksheet, employee):
        
        dtNow = datetime.datetime.now()
        punchDayTime = [dtNow.strftime("%m-%d-%Y"), dtNow.strftime("%H:%M")]
        
        redLedPin = 7
        greenLedPin = 15
        
        try:
                if dtNow.time() < datetime.time(12):
                        punch = [worksheet, employee, punchDayTime, "CLOCKIN"]
                        ledThread = threadFunction(blink, [greenLedPin, 3])

                elif dtNow.time() > datetime.time(12):
                        punch = [worksheet, employee, punchDayTime, "CLOCKOUT"]            
                        ledThread = threadFunction(blink, [greenLedPin, 6])

                cardThread = threadFunction(timeCard, [punch])
                cardThread.start()
                ledThread.start()

        except:
                blink(redLedPin, 10)

if __name__ == '__main__':
        mainSwipe(sys.argv[1], sys.argv[2])  
