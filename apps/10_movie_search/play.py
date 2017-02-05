import requests
import collections


MovieResult = collections.namedtuple(
    'MovieResult',
    'Title, Poster, Type, imdbID, Year'
)

search = 'matrix'
url = 'http://www.omdbapi.com/?t={}&y=&plot=short&r=json'.format(search)

r = requests.get(url)
data = r.json()

# def method_with_kwargs(ps1, **kwargs):
#     pass

# movies = []
# for result in results:
#     m = MovieResult(
#         Title=result['Title'],
#         Poster=result['Poster'],
#         Type=result['Type'],
#         imdbID=result['imdbID'],
#         Year=result['Year']
#     )
#     movies.append(m)

# Operates the same as above, but using kwargs
# movies = []
# for result in results:
#     m = MovieResult(**result)
#     movies.append(m)

movies = [
    MovieResult(**m)
    for m in results
]
