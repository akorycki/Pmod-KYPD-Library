import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class KYPDscanner:

    def __init__(self, COL4, COL3, COL2, COL1, ROW4, ROW3, ROW2, ROW1):
        GPIO.setup(8, GPIO.OUT)  #COL 4
        GPIO.setup(10, GPIO.OUT) #COL 3
        GPIO.setup(12, GPIO.OUT) #COL 2
        GPIO.setup(16, GPIO.OUT) #COL 1
        GPIO.setup(18, GPIO.IN)  #ROW 4
        GPIO.setup(22, GPIO.IN)  #ROW 3
        GPIO.setup(24, GPIO.IN)  #ROW 2
        GPIO.setup(26, GPIO.IN)  #ROW 1

        GPIO.output(8, True)
        GPIO.output(10, True)
        GPIO.output(12, True)
        GPIO.output(16, True)


    def scan(self):
        while True:
            GPIO.output(8, False)
            if not GPIO.input(18):
                GPIO.output(8, True)
                time.sleep(0.15)
                return ('D')
            if not GPIO.input(22):
                GPIO.output(8, True)
                time.sleep(0.15)
                return ('C')
            if not GPIO.input(24):
                GPIO.output(8, True)
                time.sleep(0.15)
                return ('B')
            if not GPIO.input(26):
                GPIO.output(8, True)
                time.sleep(0.15)
                return ('A')
            GPIO.output(8, True)

            GPIO.output(10, False)
            if not GPIO.input(18):
                GPIO.output(10, True)
                time.sleep(0.15)
                return ('E')
            if not GPIO.input(22):
                GPIO.output(10, True)
                time.sleep(0.15)
                return ('9')
            if not GPIO.input(24):
                GPIO.output(10, True)
                time.sleep(0.15)
                return ('6')
            if not GPIO.input(26):
                GPIO.output(10, True)
                time.sleep(0.15)
                return ('3')
            GPIO.output(10, True)

            GPIO.output(12, False)
            if not GPIO.input(18):
                GPIO.output(12, True)
                time.sleep(0.15)
                return ('F')
            if not GPIO.input(22):
                GPIO.output(12, True)
                time.sleep(0.15)
                return ('8')
            if not GPIO.input(24):
                GPIO.output(12, True)
                time.sleep(0.15)
                return ('5')
            if not GPIO.input(26):
                GPIO.output(12, True)
                time.sleep(0.15)
                return ('2')
            GPIO.output(12, True)

            GPIO.output(16, False)
            if not GPIO.input(18):
                GPIO.output(16, True)
                time.sleep(0.15)
                return ('0')
            if not GPIO.input(22):
                GPIO.output(16, True)
                time.sleep(0.15)
                return ('7')
            if not GPIO.input(24):
                GPIO.output(16, True)
                time.sleep(0.15)
                return ('4')
            if not GPIO.input(26):
                GPIO.output(16, True)
                time.sleep(0.15)
                return ('1')
            GPIO.output(16, True)

    def begin(self):
        while True:
            print(self.scan())
        

    def string(self):
        word = ''
        while (True):
            hex = self.scan()
            if ((hex != 'E')):
                word = word + hex
            elif (hex == 'E'):
                print(word)
                
                


