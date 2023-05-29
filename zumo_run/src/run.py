import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MOTOR_A1_PIN = 4
MOTOR_A2_PIN = 17
MOTOR_B1_PIN = 18
MOTOR_B2_PIN = 22

GPIO.setup(MOTOR_A1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_A2_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B2_PIN, GPIO.OUT)

def move_forward():
    print("forward")
    GPIO.output(MOTOR_A1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_A2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B2_PIN, GPIO.LOW)

def stop():
    print("stop")
    GPIO.output(MOTOR_A1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B2_PIN, GPIO.LOW)

try:
    move_forward()
    time.sleep(2)
    stop()
    time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
finally:
    stop()
    GPIO.cleanup()

