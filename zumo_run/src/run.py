import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PWM_FREQUENCY = 50
DUTY_CYCLE = 50

MOTOR_A1_PIN = 18
MOTOR_A2_PIN = 5
MOTOR_B1_PIN = 12
MOTOR_B2_PIN = 6

GPIO.setup(MOTOR_A1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_A2_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_B2_PIN, GPIO.OUT)

pwm_left = GPIO.PWM(MOTOR_A1_PIN, PWM_FREQUENCY)
pwm_right = GPIO.PWM(MOTOR_B1_PIN, PWM_FREQUENCY)

def move_forward():
    print("forward")

    pwm_left.start(DUTY_CYCLE)
    pwm_right.start(DUTY_CYCLE)

    GPIO.output(MOTOR_A1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_A2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B2_PIN, GPIO.LOW)

def move_backward():
    print("back")

    pwm_left.start(DUTY_CYCLE)
    pwm_right.start(DUTY_CYCLE)

    GPIO.output(MOTOR_A1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A2_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B2_PIN, GPIO.HIGH)

def move_left():
    print("left")

    pwm_left.start(DUTY_CYCLE)
    pwm_right.start(DUTY_CYCLE)

    GPIO.output(MOTOR_A1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A2_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B2_PIN, GPIO.HIGH)

def move_right():
    print("right")

    pwm_left.start(DUTY_CYCLE)
    pwm_right.start(DUTY_CYCLE)

    GPIO.output(MOTOR_A1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_A2_PIN, GPIO.HIGH)
    GPIO.output(MOTOR_B1_PIN, GPIO.LOW)
    GPIO.output(MOTOR_B2_PIN, GPIO.LOW)

def stop():
    print("stop")

    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)

try:
    move_forward()
    time.sleep(2)
    stop()
    move_backward()
    time.sleep(2)
    stop()
    move_left()
    time.sleep(2)
    stop()
    move_right()
    time.sleep(2)
    stop()
    time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
finally:
    pwm_left.stop()
    pwm_right.stop()
    stop()
    GPIO.cleanup()

