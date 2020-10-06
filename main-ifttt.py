from sense_hat import SenseHat
from ifttt import Webhook

import time


IFTTT_KEY = 'cwyhruP2opLtSGJt7bO6zi'
CHECK_SPAN = 60 * 10

sense = SenseHat()
webhook = Webhook('send_data', IFTTT_KEY)


def main():
    while True:
        payload = {
            "value1": sense.get_temperature(),
            "value2": sense.get_humidity(),
        }

        res = webhook.post(payload=payload)
        if not res.ok:
            print('Request failed with status code', res.status_code)

        time.sleep(CHECK_SPAN)


if __name__ == '__main__':
    main()
