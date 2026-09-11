# Q3
def favorite_movies(filename):
    with open(filename, 'w') as file:
        response = str(input("Enter a movie title (or 'done' to finish): ")).title()
        movies = 0

        while not response == "Done":
            movies += 1
            file.write(f"{response}\n")
            response = str(input("Enter a movie title (or 'done' to finish): ")).title()

        print(f"{movies} movies were entered")





if __name__ == "__main__":
    favorite_movies('test_files/favorites.txt')
