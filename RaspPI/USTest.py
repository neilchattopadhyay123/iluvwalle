import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 2   # GPIO 2 (Pin 3)
ECHO = 3   # GPIO 3 (Pin 5)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    """Measure distance using HC-SR04"""
    GPIO.output(TRIG, False)
    time.sleep(0.05)  # settle

    # Trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm
    return round(distance, 2)