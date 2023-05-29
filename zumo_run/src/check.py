import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)  # 시리얼 포트 및 전송 속도에 맞게 설정

def send_command(motor, speed):
    command = str(motor) + ',' + str(speed) + '\n'  # 명령 문자열 생성
    ser.write(command.encode())  # 명령 문자열을 시리얼 포트로 전송

# 모터 제어 예시
send_command(1, 100)  # 모터 1을 100의 속도로 회전
time.sleep(2)  # 2초 동안 회전
send_command(1, 0)  # 모터 1을 정지

