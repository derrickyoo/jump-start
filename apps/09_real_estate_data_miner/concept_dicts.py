lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'cat'

if 'cat' in lookup:
    print(lookup['cat'])

class Wizard:
    # This actually creates a key value dictionary
    def __init__(self, name, level):
        self.level = level
        self.name = name

# There is an implicit dictionary that stores this data
gandolf = Wizard('Gladolf', 42)
print(gandolf.__dict__)

# The takeway is that all objects are built around the concept of dictionary data structures

# Here is another example

import collections

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@test.com'),
    User(2, 'user2', 'user2@test.com'),
    User(3, 'user3', 'user3@test.com'),
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(lookup['user2@test.com'])