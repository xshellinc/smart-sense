from threading import Thread
import time

import Adafruit_DHT


class DHT22:
    def __init__(self, pin=4):
        self.dht22 = Adafruit_DHT.DHT22
        self.pin = pin
        self.temperature = None
        self.humidity = None
        self.start()
        time.sleep(2)

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()

    def update(self):
        while True:
            hum, temp = Adafruit_DHT.read_retry(self.dht22, self.pin)
            if hum is None or temp is None:
                continue
            
            self.humidity = hum
            self.temperature = temp
        
    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity


if __name__ == '__main__':
    sense = DHT22()

    for i in range(5):
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        
        print(f'====={time.ctime()}=====')
        print(f'Temperature: {temp}')
        print(f'Himidity: {hum}')

        time.sleep(2)
