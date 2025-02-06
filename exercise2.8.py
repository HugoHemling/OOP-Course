class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

def movies_of_genre(movies: list, genre: str):
    return [movie for movie in movies if movie.genre == genre]

# Example usage
john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)
hero = Movie("Hero", "Yimou Zhang", "action", 2002)

movies = [john_woo, kungfu, jet_li, hero]

print("Movies in the action genre:")
for movie in movies_of_genre(movies, "action"):
    print(f"{movie.director}: {movie.name}")
