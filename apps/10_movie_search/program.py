from movie_client import MovieClient


def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------------------------')
    print('              Movie Search App              ')
    print('--------------------------------------------')
    print()


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != 'x':
        search = input('Title search text (x to exit): ')
        if search != 'x':
            client = MovieClient(search)

            results = client.perform_search()
            print("Found {} results.".format(len(results)))
            for r in results:
                print('{} -- {}'.format(
                    r.Year, r.Title
                ))

    print('exiting...')

if __name__ == '__main__':
    main()
