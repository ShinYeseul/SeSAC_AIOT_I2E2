import RPi.GPIO as GPIO
import time
import errno
from client import *

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

TRIG = 27
ECHO = 22
print('sensor start')

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

time.sleep(2)
try:
    while True:
        passecho = False

        GPIO.output(TRIG, True)
        time.sleep(0.00001)

        GPIO.output(TRIG, False)
        # print('0')
        timeout = time.time()
        while GPIO.input(ECHO) == 0:
            start = time.time()
            if start - timeout > 3:
                break
        if passecho:
            continue
        # print('1')
        while GPIO.input(ECHO) == 1:
            stop = time.time()
            if stop - start > 3:
                break

        check_time = stop - start

        distance = check_time * 34300 / 2
        print('Distance : %1.f cm' % distance)
        c_socket.sendall(str(distance).encode())

        time.sleep(0.5)


except KeyboardInterrupt:
    print("sensor end")
    GPIO.cleanup()