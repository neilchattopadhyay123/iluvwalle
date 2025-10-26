import RPi.GPIO as GPIO
import time

# --- GPIO Mode (BOARD / BCM) ---
GPIO.setmode(GPIO.BCM)

# --- Define Pins ---
TRIG = 23
ECHO = 24

# --- Set Pin Directions ---
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Ensure trigger is LOW
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Send a short 10µs pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for echo to go HIGH
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo to go LOW
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Calculate distance (speed of sound = 34300 cm/s)
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
