from time import sleep

import requests

URL = "http://airborne.gogoinflight.com/abp/ws/absServices/statusTray"


def get_info():
    response = requests.get(URL)
    return response.json().get("Response")


def main():
    x, y = list(), list()
    try:
        while True:
            try:
                response = get_info().get("flightInfo")
            except requests.exceptions.ConnectionError:
                break
            # hspeed = response.get("hspeed")
            altitude = response.get("altitude")
            x.append(altitude)
            y.append(len(x))
            print(altitude)
            sleep(5)
    except KeyboardInterrupt:
        print("Plotting...")

    import matplotlib.pyplot as plt

    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.title("Flight Info")

    plt.plot(y, x)
    plt.show()


if __name__ == "__main__":
    main()
