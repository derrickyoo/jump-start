from movie_client import MovieClient
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------------------------')
    print('              Movie Search App              ')
    print('--------------------------------------------')
    print()


def search_event_loop():
    search_text = "ONCE_THROUGH_LOOP"

    while search_text != 'x':
        try:
            search_text = input('Title search text (x to exit): ')

            if search_text != 'x':
                client = MovieClient(search_text)

                results = client.perform_search()
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.Year, r.Title
                    ))
        except requests.exceptions.ConnectionError:
            print('ERROR: Cannot search, your network is down.')
        except ValueError as ve:
            print('ERROR: Your search text is invalid: {}'.format(ve))
        except Exception as x:
            print('That did not work: {}'.format(x));

    print('exiting...')

if __name__ == '__main__':
    main()
