import RPi.GPIO as GPIO
import time

channelkipas = 23
channellampu = 24

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channelkipas, GPIO.OUT)
GPIO.setup(channellampu, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    try:
        motor_on(channelkipas)
        time.sleep(1)
        motor_off(channelkipas)
        time.sleep(60)
        GPIO.cleanup()
        motor_on(channellampu)
        time.sleep(1)
        motor_off(channellampu)
        time.sleep(25)
        GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

