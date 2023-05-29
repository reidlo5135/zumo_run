import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
motor_pin1 = 7
motor_pin2 = 8
motor_pwm_pin = 9
motor_standby_pin = 10

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(motor_pwm_pin, GPIO.OUT)
GPIO.setup(motor_standby_pin, GPIO.OUT)

# 모터 제어 함수
def control_motor(speed):
    # 모터 방향 설정
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, GPIO.LOW)

    # PWM 설정
    pwm = GPIO.PWM(motor_pwm_pin, 100)  # PWM 주파수 설정 (100Hz)
    pwm.start(speed)  # 모터 속도 설정 (0 ~ 100)

    # 일정 시간 동안 동작 후 멈춤
    time.sleep(2)

    # 모터 정지
    GPIO.output(motor_standby_pin, GPIO.LOW)
    pwm.stop()

# 모터 동작 테스트
control_motor(50)  # 속도 50%로 모터 동작

