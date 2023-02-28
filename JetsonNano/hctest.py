import Jetson.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

TRIG=13
ECHO=12
print("초음파 거리 측정기")

GPIO.setup(TRIG, GPIO.OUT, initial=False)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("초음파 출력 초기화")
time.sleep(2)
try:
    while True:
        passecho = False

        GPIO.output(TRIG,True)
        time.sleep(0.00001)        

        GPIO.output(TRIG,False)
        print('0')
        timeout = time.time()
        while GPIO.input(ECHO)==0:
            start = time.time()
            if start - timeout > 3:
                break
        if passecho:
            continue
        print('1')
        while GPIO.input(ECHO)==1:
            stop = time.time()     
            if stop - start > 3:
                break


        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance : %.1f cm" % distance)
        time.sleep(0.5)        

except KeyboardInterrupt:
    print("거리 측정 완료 ")
    GPIO.cleanup()
