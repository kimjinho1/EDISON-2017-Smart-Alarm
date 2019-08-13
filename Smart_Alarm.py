import RPi.GPIO as GPIO
from time import sleep

GPIO. setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(18 , GPIO.IN)

alarm = True # 알람
button = True # 버튼 센서
touch = True # 터치 센서
rain = True # 우적(Rain) 센서

try:
    while(alarm): # 알람 시작
        GPIO.setmode(GPIO.BCM)
        BUZ = 15
        ON = 1
        oFF = 0

        GPIO.setup(BUZ, GPIO.OUT)
        ck_pwm = GPIO.PWM(BUZ, 1000)
        ck_pwm.start(50)
#        time.sleep(5)
#        ck_pwm.stop()

        while(button): # 버튼을 눌러야 반복문 나감
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            inputIO = GPIO.input(26)
            if(inputIO == 0):
                GPIO.output(13, GPIO.LOW)
                print("switch")
                button = False
        

        while(touch): # 터치 센서를 만져야 반복문 나감
            pad_pressed = GPIO.input(pin_num)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            if(pad_pressed):
                print("Touch")
                touch = False
                GPIO.output(19, GPIO.LOW)
                sleep(0.1)


        while(rain): # 우적 센서에 물을 묻혀야 반복문 나감
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            inputIO = GPIO.input(21)

            if(inputIO == False):
                GPIO.output(6, GPIO.LOW)
                print("rain")
                rain = False
                alarm = False # 전체 반복문 나가므로 알람 꺼짐
                GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
