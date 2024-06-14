import random

class CineMatch:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre):
        rating = random.randint(1, 10)
        self.movies.append({"title": title, "genre": genre, "rating": rating})

    def search_by_title(self, title):
        return [movie for movie in self.movies if title.lower() in movie['title'].lower()]

    def search_by_genre(self, genre):
        return [movie for movie in self.movies if genre.lower() in movie['genre'].lower()]

    def recommend_top_n(self, n):
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        return sorted_movies[:n]

    def delete_movie(self, title):
        self.movies = [movie for movie in self.movies if movie['title'].lower() != title.lower()]
