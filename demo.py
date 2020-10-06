import time

from sense_hat import SenseHat


sense = SenseHat()


def main():
    sense.clear(128, 128, 128)

    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        pres = sense.get_pressure()
        print(f'====={time.ctime()}=====')
        print(f'Temperature: {temp}')
        print(f'Humidity: {hum}')
        print(f'Pressure: {pres}')

        events = []
        for event in sense.stick.get_events():
            events.append([event.action, event.direction])
        print(f'Events: {events}')

        time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sense.clear()
