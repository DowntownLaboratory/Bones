import RPi.GPIO as GPIO
import time

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    print ('enabling led%d'%ledPin)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print ('enabling button%d'%buttonPin)

def buttonEvent(channel):
    global ledState
    print ('buttonEvent GPIO%d' %channel)
    ledState = not ledState
    if(ledState):
        print('led on')
    else:
        print('led off')

    GPIO.output(ledPin, ledState)

def loop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime=300)
    while True:
        pass

def destroy():
    GPIO.cleanup() # Release all GPIO

if __name__ == '__main__': # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()