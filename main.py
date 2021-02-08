import json
import movies_search
import save
#import os

movies = movies_search.Movie()


def main():
    while True:
        print(70 * "=")
        choice = input("\t\tWelcome, please choose a menu\n\n"
                       "\t\t1. Search Movie\n"
                       "\t\t2. View Recently \n"
                       "\t\t3. Exit\n")
        if choice == "1":
            movies.search_movies()
            movies.print_info()
            movies.print_movie_info()
        elif choice == "2":
            print(save.History.read_json("history.json"))
        elif choice == "3":
           # print(os.stat("history.json").st_size)
            print("Program exit!")
            print(70 * "=")
            quit()
        else:
            print("\nSorry, but", choice,  "is not a valid choice.\n")


main()
