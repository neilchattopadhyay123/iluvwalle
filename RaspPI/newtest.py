import RPi.GPIO as GPIO
import time

# --- CONFIGURE YOUR SENSOR PINS ---
TRIG = 23
ECHO = 24

# --- SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("\n[SETUP] GPIO Debugging Script Initialized")
print(f"[INFO] TRIG pin: GPIO {TRIG}")
print(f"[INFO] ECHO pin: GPIO {ECHO}\n")

# --- SAFELY SET SENSOR PINS ---
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# --- HELPER FUNCTIONS ---

def check_pin_states():
    """Check all available GPIO pins and show if they are HIGH or LOW."""
    print("[SCAN] Checking all GPIO pin states...\n")
    for pin in range(2, 28):  # Typical usable GPIO range
        try:
            GPIO.setup(pin, GPIO.IN)
            state = GPIO.input(pin)
            print(f"GPIO {pin:>2}: {'HIGH' if state else 'LOW'}")
        except Exception as e:
            print(f"GPIO {pin:>2}: [ERROR] {e}")
    print("\n[SCAN] Finished checking GPIO pins.\n")


def test_trig_pin():
    """Test that TRIG pin can go HIGH and LOW."""
    print(f"[TEST] Testing TRIG pin (GPIO {TRIG})...")
    try:
        GPIO.setup(TRIG, GPIO.OUT)  # Make sure it's output
        GPIO.output(TRIG, False)
        print("[ACTION] Setting TRIG HIGH for 1 second...")
        GPIO.output(TRIG, True)
        time.sleep(1)
        state = GPIO.input(TRIG)
        print(f"[RESULT] TRIG now reads: {'HIGH' if state else 'LOW'}")
        GPIO.output(TRIG, False)
        print("[DONE] TRIG test complete.\n")
    except Exception as e:
        print(f"[ERROR] TRIG test failed: {e}\n")


def monitor_echo_pin(duration=5):
    """Monitor the ECHO pin for any signal changes."""
    print(f"[MONITOR] Watching ECHO pin (GPIO {ECHO}) for {duration} seconds...")
    GPIO.setup(ECHO, GPIO.IN)
    start = time.time()
    prev_state = GPIO.input(ECHO)
    changes = 0

    while time.time() - start < duration:
        state = GPIO.input(ECHO)
        if state != prev_state:
            changes += 1
            print(f"[ECHO] State changed to: {'HIGH' if state else 'LOW'} at {time.time() - start:.3f}s")
            prev_state = state
        time.sleep(0.01)

    if changes == 0:
        print("[WARNING] ECHO pin did not change — no signal detected!")
    else:
        print(f"[INFO] ECHO pin changed state {changes} times during monitoring.\n")


# --- MAIN EXECUTION ---
try:
    check_pin_states()
    test_trig_pin()
    monitor_echo_pin()

except KeyboardInterrupt:
    print("\n[EXIT] Stopped by user.")

finally:
    GPIO.cleanup()
    print("[CLEANUP] GPIO reset complete. Exiting safely

