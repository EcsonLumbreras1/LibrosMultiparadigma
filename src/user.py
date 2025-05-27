class User:
    def __init__(self, username, favorite_genres=None, favorite_authors=None):
        self.username = username
        self.favorite_genres = favorite_genres if favorite_genres else []
        self.favorite_authors = favorite_authors if favorite_authors else []

    def add_genre(self, genre):
        if genre not in self.favorite_genres:
            self.favorite_genres.append(genre)

    def add_author(self, author):
        if author not in self.favorite_authors:
            self.favorite_authors.append(author)

    def __str__(self):
        return f"User: {self.username}, Favorite Genres: {self.favorite_genres}, Favorite Authors: {self.favorite_authors}"
