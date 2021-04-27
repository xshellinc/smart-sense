from sense_hat import SenseHat as Sensor
#from sense_emu import SenseHat as Sensor
#from dht22 import DHT22 as Sensor

import csv
import time
from datetime import datetime


TEMP_DELTA = 0
CHECK_SPAN = 10

sense = Sensor()


def main():
    while True:
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        temp = sense.get_temperature() - TEMP_DELTA
        hum = sense.get_humidity()
        row = [now, temp, hum]
        
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            
        time.sleep(CHECK_SPAN)


if __name__ == '__main__':
    main()
