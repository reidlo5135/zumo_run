import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 4

GPIO.setup(BUZZER_PIN, GPIO.OUT)

def turn_on_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

def turn_off_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.LOW)

try:
    turn_on_buzzer()
    time.sleep(2)
    turn_off_buzzer()
    time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
finally:
    turn_off_buzzer()
    GPIO.cleanup()

