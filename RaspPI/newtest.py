import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)      # Use PHYSICAL pin numbering
GPIO.setwarnings(False)

pin = 9  # Physical pin 9 (Ground)

# Set as input (safe)
GPIO.setup(pin, GPIO.IN)

val = GPIO.input(pin)
print(f"Physical pin {pin} reads:", val)
print("Expected value: 0 (since this pin is GROUND)")

GPIO.cleanup()


