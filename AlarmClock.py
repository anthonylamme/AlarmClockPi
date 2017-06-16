import RPi.GPIO as GPIO
import time

alarmtimes=[928,1228,1628,190,1109,1110]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
def cleanup():
        GPIO.cleanup()

try:
        while True:
                localtime = time.localtime(time.time())
                alarm = list(localtime)
                alarm = alarm[3:5]
                alarm = ''.join(str(x) for x in alarm)
                alarm =int(alarm)
                print "%d\n"%alarm
                if alarm in alarmtimes:
                        print "yes %d" %alarm
                        GPIO.output(12,False)
                        time.sleep(4)
                        GPIO.output(12,True)
                        time.sleep(56)	
                else:
                        GPIO.output(12,True)
                        print "nope %d" %alarm
                        time.sleep(60)
                        pass
except KeyboardInterrupt:
        cleanup()
        print '\nStopping Script'
except:
        print 'debug code'
finally:
        cleanup()
