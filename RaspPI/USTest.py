import RPi.GPIO as GPIO
import time
import machine

# --- Setup ---
GPIO.setmode(GPIO.BCM)

TRIG = 23   # GPIO 2 (Pin 3)
ECHO = 24   # GPIO 3 (Pin 5)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Starting distance measurement...")
time.sleep(2)

def get_distance():
    # Ensure trigger is low
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Send 10 µs trigger pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # in cm
    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user.")

finally:
    GPIO.cleanup()