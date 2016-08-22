import requests


def main():
    print_header()
    zip_code = input('Enter ZIP code: ')
    html = get_html_weather_from_web(zip_code)
    # parse the html
    # display forcast


def print_header():
    print('------------------------------------------')
    print('           Weather Client App             ')
    print('------------------------------------------')
    print()


def get_html_weather_from_web(zip_code):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)

    return response


def parse_html_from_web():
    pass


def display_forcast():
    pass


if __name__ == "__main__":
    main()
