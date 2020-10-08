from sense_hat import SenseHat
#from sense_emu import SenseHat
from ifttt import Webhook

import time
from datetime import datetime


IFTTT_KEY = ''
TEMP_DELTA = 0
CHECK_SPAN = 60 * 10

sense = SenseHat()
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
