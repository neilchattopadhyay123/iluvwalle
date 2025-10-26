import RPi.GPIO as GPIO
import time

# --- CONFIGURE PINS ---
TRIG = 23
ECHO = 24

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("\n[SETUP] GPIO Debugging Script Initialized")
print(f"[INFO] TRIG pin: GPIO {TRIG}")
print(f"[INFO] ECHO pin: GPIO {ECHO}")
print("[INFO] Checking GPIO status...\n")

# --- HELPER FUNCTIONS ---

def check_pin_states():
    print("[SCAN] Reading GPIO pin states...")
    for pin in range(2, 28):  # Valid GPIO range for most Pi models
        try:
            GPIO.setup(pin, GPIO.IN)
            state = GPIO.input(pin)
            print(f"GPIO {pin}: {'HIGH' if state else 'LOW'}")
        except Exception as e:
            print(f"GPIO {pin}: [ERROR] {e}")
    print("[SCAN] Done checking all pins.\n")

def test_trig_pin():
    print(f"[TEST] Testing TRIG pin (GPIO {TRIG})...")
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    print("[ACTION] Setting TRIG HIGH for 1 second...")
    GPIO.output(TRIG, True)
    time.sleep(1)
    trig_state = GPIO.input(TRIG)
    print(f"[RESULT] TRIG pin now reads: {'HIGH' if trig_state else 'LOW'}")
    GPIO.output(TRIG, False)
    print("[DONE] TRIG test complete.\n")

def monitor_echo_pin(duration=5):
    print(f"[MONITOR] Watching ECHO pin (GPIO {ECHO}) for {duration} seconds...")
    start = time.time()
    prev_state = None
    changes = 0

    while time.time() - start < duration:
        state = GPIO.input(ECHO)
        if state != prev_state:
            changes += 1
            print(f"[ECHO] State changed to: {'HIGH' if state else 'LOW'}")
            prev_state = state
        time.sleep(0.01)

    if changes == 0:
        print("[WARNING] ECHO pin did not change — no signal detected!")
    else:
        print(f"[INFO] ECHO pin changed state {changes} times during monitoring.\n")

# --- RUN TESTS ---
try:
    check_pin_states()
    test_trig_pin()
    monitor_echo_pin()

except KeyboardInterrupt:
    print("\n[EXIT] Stopped by user.")

finally:
    GPIO.cleanup()
    print("[CLEANUP] GPIO reset complete. Exiting safely.")
