#!/usr/bin/env python3
########################################################################
# Filename    : UnipolarRev.py
# Author      : danelu
# modification: 2018/08/02
# ReverseOnly
########################################################################
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
# motorPins = (11, 16, 18, 22, physical)    #define pins connected to four phase ABCD of stepper motor
GPIO.setwarnings(False)
pin1 = 17
pin2 = 22
pin3 = 23
pin4 = 24

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

t1 = 0.003  # power time for energizing the coils
# t = input ("Speed?/msecs 0=max; 50=min " )
# tp=int(t)
t2 = 0.003  # pause time between pulses


def setStep(w1, w2, w3, w4):
    GPIO.output(pin1, w4)
    GPIO.output(pin2, w3)
    GPIO.output(pin3, w2)
    GPIO.output(pin4, w1)

if len(sys.argv) == 1:
    n = input("Steps? ")  # how many steps to execute
else:
    n = sys.argv[1]
m = int(n)

for i in range(0, m):
    setStep(1, 0, 0, 0)
    time.sleep(t1)
    setStep(0, 0, 0, 0)
    time.sleep(t2)

    setStep(0, 1, 0, 0)
    time.sleep(t1)
    setStep(0, 0, 0, 0)
    time.sleep(t2)

    setStep(0, 0, 1, 0)
    time.sleep(t1)
    setStep(0, 0, 0, 0)
    time.sleep(t2)

    setStep(0, 0, 0, 1)
    time.sleep(t1)
    setStep(0, 0, 0, 0)
    time.sleep(t2)
