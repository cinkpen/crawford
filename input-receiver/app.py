import time
import logging

import RPi.GPIO as GPIO

# Setup logging
logging.basicConfig(filename='/home/pi/crawford/input-receiver/gpio.log', level=logging.INFO, format='%(asctime)s - %(message)s')

gpio_in = 26


# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def log_event(channel):
    print(channel)
    if GPIO.input(channel):
        s = f'GPIO {gpio_in} Triggered'
        logging.info(s)
    else:
        s = f'GPIO {gpio_in} Untriggered'
        logging.info(s)

# Add event detection
GPIO.add_event_detect(gpio_in, GPIO.BOTH, callback=log_event, bouncetime=2)

try:
    while True:
        time.sleep(1)
        print(".")
except KeyboardInterrupt:
    GPIO.cleanup()
