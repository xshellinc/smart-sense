from sense_hat import SenseHat as Sensor
#from sense_emu import SenseHat as Sensor
#from dht22 import DHT22 as Sensor
from ifttt import Webhook

import time
from datetime import datetime


IFTTT_KEY = ''
TEMP_DELTA = 0
CHECK_SPAN = 60 * 10

sense = Sensor()
webhook = Webhook('send_data', IFTTT_KEY)


def main():
    while True:
        payload = {
            "value1": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            "value2": sense.get_temperature() - TEMP_DELTA,
            "value3": sense.get_humidity(),
        }

        res = webhook.post(payload=payload)
        if not res.ok:
            print('Request failed with status code', res.status_code)

        time.sleep(CHECK_SPAN)


if __name__ == '__main__':
    main()
