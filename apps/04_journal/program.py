import journal


def main():
    print_header()
    run_event_loop()
    pass


def print_header():
    print('------------------------------------------')
    print('           Personal Journal App           ')
    print('------------------------------------------')
    print()


def run_event_loop():
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name) #[] # list()


    while cmd != 'x':
        cmd = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print('Sorry, we don\'t understand {}'.format(cmd))

    print('Done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{0}] - {1}'.format(idx+1, entry))


def add_entry(data):
    text = input ('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
