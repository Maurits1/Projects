import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

groen = 21
geel = 20
rood = 19
trigger = 23
echo = 24


GPIO.setup(groen,GPIO.OUT)
GPIO.setup(geel,GPIO.OUT)
GPIO.setup(rood,GPIO.OUT)
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)



def groen_aan():
    GPIO.output(groen,GPIO.HIGH)
    GPIO.output(geel,GPIO.LOW)
    GPIO.output(rood,GPIO.LOW)

def geel_aan():
    GPIO.output(groen,GPIO.LOW)
    GPIO.output(geel,GPIO.HIGH)
    GPIO.output(rood,GPIO.LOW)

def rood_aan():
    GPIO.output(groen,GPIO.LOW)
    GPIO.output(geel,GPIO.LOW)
    GPIO.output(rood,GPIO.HIGH)
#
# while True:
#         groen_aan()
#         time.sleep(0.1)
#         geel_aan()
#         time.sleep(0.1)
#         rood_aan()
#         time.sleep(0.1)
#         geel_aan()
#         time.sleep(0.1)

GPIO.output(trigger,GPIO.LOW)
time.sleep(2)
try:
    while True:
        GPIO.output(trigger,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger,GPIO.LOW)

        while GPIO.input(echo)==0:
            pulse_start_time=time.time()
        while GPIO.input(echo)==1:
            pulse_end_time=time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print "distance: ", distance, " cm"

        if distance < 11:
            groen_aan()
        elif 10 < distance < 30:
            geel_aan()
        elif distance > 30:
            rood_aan()

        time.sleep(0.2)
finally:
    GPIO.cleanup()
