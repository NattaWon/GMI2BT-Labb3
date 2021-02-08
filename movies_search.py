import requests
from requests.models import Response as res
import save
import json


class Movie():
    def search_movies(self):
        movie_search = input("Search for a movie: ")
        save.History.write_json("history.json", movie_search)
        movieinfo = requests.get(
            f"http://www.omdbapi.com/?apikey=fe22435b&s={movie_search}")
        data = movieinfo.json()
        if data["Response"] == "True":
            self.movies = data['Search']
        else:
            print("No movies found")

    def print_info(self):
        for m in range(len(self.movies)):  # def skriver all movies
            print(f"{m+1}.{self.movies[m]['Title']}.{self.movies[m]['Year']}")
        self.movie_info = int(input("Choose a movie: "))

    def print_movie_info(self):
        for i in range(len(self.movies)):  # def skriver ut till konsolen
            if i+1 == self.movie_info:
                print(self.movies[i])
        self.show_movie()

    def show_movie(self):
        movieID = self.movies[self.movie_info]
        movieinfo = requests.get(
            f"http://www.omdbapi.com/?apikey=fe22435b&i={movieID['imdbID']}")
        data = movieinfo.json()
        print(data['Title'], data['Plot'])
