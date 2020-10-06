from sense_hat import SenseHat

from datetime import datetime
import csv
import time


sense = SenseHat()


def main():
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        created_at = datetime.now().isoformat()
        row = [temp, hum, created_at]

        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)

        time.sleep(5)


if __name__ == '__main__':
    main()
