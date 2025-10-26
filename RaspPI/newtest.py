import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # Important!
pin = 9  # Physical pin 9
GPIO.setup(pin, GPIO.IN)
print("Reading from physical pin 9:", GPIO.input(pin))

