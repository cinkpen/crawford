#!/usr/bin/env python3
import time
import json
from dotenv import load_dotenv
import os
import logging

import RPi.GPIO as GPIO
from pa1010d import PA1010D

load_dotenv()


gps = PA1010D(debug=True)
fileName = '/home/admin/crawford/gps-receiver/litter.log'

 
# Setup logging
logging.basicConfig(filename=fileName, level=logging.INFO, format='%(asctime)s - %(message)s')

gpio_in = 26
# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

logging.info("Startup")




def log_event(channel):
    print(f'Channel {channel} event detected')
    input_state = GPIO.input(channel)
    print(f'Input state: {input_state}')
    if input_state:
        s = f'GPIO {gpio_in} Triggered'
        print(s)
        logging.info(s)
    else:
        s = f'GPIO {gpio_in} Untriggered'
        logging.info(s)

# Add event detection
GPIO.add_event_detect(gpio_in, GPIO.BOTH, callback=log_event, bouncetime=200)


while True:
    result = gps.update()
    j = {
        "timestamp": str(gps.data['timestamp']),
        "latitude": gps.data['latitude'],
        "longitude": gps.data['longitude'],
        "altitude": gps.data['altitude'],
        "num_sats": gps.data['num_sats'],
        "gps_qual": gps.data['gps_qual'],
        "speed_over_ground": gps.data['speed_over_ground'],
        "mode_fix_type": gps.data['mode_fix_type'],
        "pdop": gps.data['pdop'],
        "vdop": gps.data['vdop'],
        "hdop": gps.data['hdop']
    }
    if result:
        print(j)
        logging.info(j)

    time.sleep(5.0)
