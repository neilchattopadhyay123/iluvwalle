import RPi.GPIO as GPIO
import time

# --- GPIO Mode ---
GPIO.setmode(GPIO.BCM)

# --- Define Pins ---
TRIG = 23
ECHO = 24

print("[SETUP] Initializing GPIO pins...")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print(f"[SETUP] TRIG pin set to GPIO {TRIG}")
print(f"[SETUP] ECHO pin set to GPIO {ECHO}")
print("[SETUP] Sensor ready.\n")

def get_distance(timeout=0.02):
    """
    Returns distance in cm or None if no signal detected.
    timeout: maximum time to wait for signal (seconds)
    """
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    # Send a short pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    pulse_start = pulse_end = None

    # Wait for ECHO HIGH
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start - start_time > timeout:
            # No HIGH detected
            return None

    # Wait for ECHO LOW
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end - pulse_start > timeout:
            # Stayed HIGH too long (invalid)
            return None

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm
    return round(distance, 2)

try:
    print("[SYSTEM] Starting continuous measurement (Ctrl+C to stop)\n")
    while True:
        dist = get_distance()

        if dist is None:
            print("[WARNING] NO SIGNAL — Object too far or sensor disconnected.")
        else:
            print(f"[OUTPUT] Distance: {dist} cm")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n[EXIT] Measurement stopped by user. Cleaning up GPIO...")
    GPIO.cleanup()
    print("[DONE] GPIO cleanup complete. Exiting safely.")
