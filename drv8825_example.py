from time import sleep
import RPi.GPIO as GPIO

DIR = 20    # Direction GPIO pin
STEP = 21   # Step GPIO pin
CW = 1      # Clockwise rotation
CCW = 0     # Counterclockwise rotation
SPR = 48    # Steps per revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.208

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()

