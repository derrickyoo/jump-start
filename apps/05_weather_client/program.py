import bs4
import requests
import collections

WeatherReport = collections.namedtuple(
    'WeatherReport',
    'location, condition, temperature, scale'
)


def main():
    print_header()
    zip_code = input('Enter ZIP code: ')
    html = get_html_weather_from_web(zip_code)
    report = get_weather_from_html(html)

    print('The weather in {} is {} and {} {}.'.format(report.location,
                                                      report.condition,
                                                      report.temperature,
                                                      report.scale))


def print_header():
    print('------------------------------------------')
    print('           Weather Client App             ')
    print('------------------------------------------')
    print()


def get_html_weather_from_web(zip_code):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temperature = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    temperature = cleanup_text(temperature)
    scale = cleanup_text(scale)

    report = WeatherReport(location=location,
                           condition=condition,
                           temperature=temperature,
                           scale=scale)

    return report


def find_city_and_state_from_location(location: str):
    parts = location.split('\n')

    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()

    return text


def display_forcast():
    pass


if __name__ == "__main__":
    main()
