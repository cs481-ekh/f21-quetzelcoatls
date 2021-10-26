#!/usr/bin/env python3
########################################################################
# Filename    : UnipolarFWD.py
# Author      : danelu
# modification: 2018/08/02
# ForwardOnly
########################################################################
# import RPi.GPIO as GPIO
import time
import sys


def do_steps_fwd(args):
    t1 = 0.003  # power time to energize each coil
    # t = input ("Speed?/msecs 0=max; 50=min " )
    # tp=int(t)
    t2 = 0.003  # pause time

    def setStep(w1, w2, w3, w4):
        time.sleep(0.0025)

    if args == "":
        args = input("Steps? ")  # how many steps to execute
    m = int(args)
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


if __name__ == '__main__':
    do_steps_fwd("") if len(sys.argv) == 1 else do_steps_fwd(sys.argv[1])
