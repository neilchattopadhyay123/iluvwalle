import RPi.GPIO as GPIO
import time

# --- GPIO Mode ---
GPIO.setmode(GPIO.BCM)

# --- Define Pins ---
TRIG = 23
ECHO = 24

print("[SETUP] Initializing GPIO pins...")

# --- Set Pin Directions ---
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print(f"[SETUP] TRIG pin set to GPIO {TRIG}")
print(f"[SETUP] ECHO pin set to GPIO {ECHO}")
print("[SETUP] Sensor ready.\n")

def get_distance():
    print("[INFO] Starting distance measurement...")

    # Make sure trigger is LOW
    GPIO.output(TRIG, False)
    print("[DEBUG] Set TRIG LOW to stabilize sensor")
    time.sleep(0.05)

    # Send a 10µs pulse to trigger
    print("[ACTION] Sending 10µs pulse to TRIG")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    print("[WAIT] Waiting for ECHO HIGH signal...")

    # Wait for ECHO HIGH
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    print("[DETECTED] ECHO HIGH detected. Waiting for LOW...")

    # Wait for ECHO LOW
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    print(f"[CALC] Pulse duration: {pulse_duration:.6f} seconds")

    # Calculate distance (speed of sound = 34300 cm/s)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print(f"[RESULT] Calculated distance: {distance} cm\n")

    return distance

try:
    print("[SYSTEM] Starting continuous measurement (press Ctrl+C to stop)\n")
    while True:
        dist = get_distance()
        print(f"[OUTPUT] Distance: {dist} cm\n")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[EXIT] Measurement stopped by user. Cleaning up GPIO...")
    GPIO.cleanup()
    print("[DONE] GPIO cleanup complete. Exiting safely.")

