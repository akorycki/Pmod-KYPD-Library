import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class KYPDscanner:

    def __init__(self, COL4, COL3, COL2, COL1, ROW4, ROW3, ROW2, ROW1):
        self.COL4 = COL4
        self.COL3 = COL3
        self.COL2 = COL2
        self.COL1 = COL1
        self.ROW4 = ROW4
        self.ROW3 = ROW3
        self.ROW2 = ROW2
        self.ROW1 = ROW1
        
        GPIO.setup(COL4, GPIO.OUT) #COL 4
        GPIO.setup(COL3, GPIO.OUT) #COL 3
        GPIO.setup(COL2, GPIO.OUT) #COL 2
        GPIO.setup(COL1, GPIO.OUT) #COL 1
        GPIO.setup(ROW4, GPIO.IN)  #ROW 4
        GPIO.setup(ROW3, GPIO.IN)  #ROW 3
        GPIO.setup(ROW2, GPIO.IN)  #ROW 2
        GPIO.setup(ROW1, GPIO.IN)  #ROW 1

        GPIO.output(self.COL4, True)
        GPIO.output(self.COL3, True)
        GPIO.output(self.COL2, True)
        GPIO.output(self.COL1, True)


    def scan(self):
        while True:
            GPIO.output(self.COL4, False)
            if not GPIO.input(self.ROW4):
                GPIO.output(self.COL4, True)
                return ('D')
            if not GPIO.input(self.ROW3):
                GPIO.output(self.COL4, True)
                return ('C')
            if not GPIO.input(self.ROW2):
                GPIO.output(self.COL4, True)
                return ('B')
            if not GPIO.input(self.ROW1):
                GPIO.output(self.COL4, True)
                return ('A')
            GPIO.output(self.COL4, True)

            GPIO.output(self.COL3, False)
            if not GPIO.input(self.ROW4):
                GPIO.output(self.COL3, True)
                return ('E')
            if not GPIO.input(self.ROW3):
                GPIO.output(self.COL3, True)
                return ('9')
            if not GPIO.input(self.ROW2):
                GPIO.output(self.COL3, True)
                return ('6')
            if not GPIO.input(self.ROW1):
                GPIO.output(self.COL3, True)
                return ('3')
            GPIO.output(self.COL3, True)

            GPIO.output(self.COL2, False)
            if not GPIO.input(self.ROW4):
                GPIO.output(self.COL2, True)
                return ('F')
            if not GPIO.input(self.ROW3):
                GPIO.output(self.COL2, True)
                return ('8')
            if not GPIO.input(self.ROW2):
                GPIO.output(self.COL2, True)
                return ('5')
            if not GPIO.input(self.ROW1):
                GPIO.output(self.COL2, True)
                return ('2')
            GPIO.output(self.COL2, True)

            GPIO.output(self.COL1, False)
            if not GPIO.input(self.ROW4):
                GPIO.output(self.COL1, True)
                return ('0')
            if not GPIO.input(self.ROW3):
                GPIO.output(self.COL1, True)
                return ('7')
            if not GPIO.input(self.ROW2):
                GPIO.output(self.COL1, True)
                return ('4')
            if not GPIO.input(self.ROW1):
                GPIO.output(self.COL1, True)
                return ('1')
            GPIO.output(self.COL1, True)

    def echo(self):
        while True:
            print(self.scan())
            time.sleep(0.2)
                
        

    def string(self):
        word = ''
        while (True):
            hex = self.scan()
            time.sleep(0.2)
            if ((hex != 'E')):
                word = word + hex
            elif (hex == 'E'):
                print(word)
