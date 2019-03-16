import requests


def get_location_info():
    return requests.get("http://geoip.makerbot.com/json/").json()


if __name__ == "__main__":
    print(get_location_info())
