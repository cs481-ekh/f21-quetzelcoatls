#!/usr/bin/env python3
# ReverseOnly
import time
import sys

t1 = 0.003  # power time for energizing the coils
# t = input ("Speed?/msecs 0=max; 50=min " )
# tp=int(t)
t2 = 0.003  # pause time between pulses


def setStep(w1, w2, w3, w4):
    pass

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
