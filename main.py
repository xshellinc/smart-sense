from sense_hat import SenseHat as Sensor
#from dht22 import DHT22 as Sensor


sense = Sensor()


def main():
    temp = sense.get_temperature()
    hum = sense.get_humidity()

    print(f'Temperature: {temp}, Humidity: {hum}')


if __name__ == '__main__':
    main()
