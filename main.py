from sense_hat import SenseHat


sense = SenseHat()


def main():
    temp = sense.get_temperature()
    hum = sense.get_humidity()

    print(f'Temperature: {temp}, Humidity: {hum}')


if __name__ == '__main__':
    main()
