from argparse import ArgumentParser

import requests

from .consts import MAPS, URLS


def try_urls(urls=URLS):
    for url in urls:
        try:
            response = requests.get(url)
            return response.json()
        except (requests.exceptions.ConnectionError, ValueError):
            continue
    print("Failed to gather information")
    exit(1)


def format_value(value):
    if isinstance(value, str):
        if value.startswith("0"):
            try:
                value = str(int(value))
            except (TypeError, ValueError):
                pass
    return value


def print_stat(title, value):
    if title and value:
        value = format_value(value)
        print("{title}: {value}".format(title=title, value=value))


def map_values(response, map):
    for map_key, map_value in map.items():
        if isinstance(map_value, dict):
            sub_dict = response.get(map_key)
            for k, v in map_value.items():
                title = v
                value = sub_dict.get(k)
                print_stat(title, value)
        else:
            title = map_value
            value = response.get(map_key)
            print_stat(title, value)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-j", "--json", help="Prints raw JSON response", action="store_true")
    args = parser.parse_args()

    response = try_urls()
    if args.json:
        print(json)
    else:
        map = MAPS[1]
        if "Response" in response.keys():
            response = response.get("Response")
            map = MAPS[0]

        map_values(response, map)


if __name__ == "__main__":
    main()
