import csv
from urllib.request import urlretrieve
from collections import namedtuple, Counter, defaultdict
import ssl

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data):
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def main():
    movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
    movies_csv = 'movies.csv'
    ssl._create_default_https_context = ssl._create_unverified_context
    urlretrieve(movie_data, movies_csv)

    directors = get_movies_by_director(movies_csv)
    print()
    print("Example showing movies directed by Christopher Nolan...")
    print(directors['Christopher Nolan'])
    print()

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print("Example showing Top 5 movies using the collections module Counter function...")
    print(cnt.most_common(5))


if __name__ == '__main__':
    main()
