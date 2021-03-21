from sense_hat import SenseHat
#from dht22 import DHT22


sense = SenseHat()
#sense = DHT22()


def main():
    temp = sense.get_temperature()
    hum = sense.get_humidity()

    print(f'Temperature: {temp}, Humidity: {hum}')


if __name__ == '__main__':
    main()
