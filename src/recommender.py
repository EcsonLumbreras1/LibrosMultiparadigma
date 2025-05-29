from book import Book

class BookRecommender:
    def __init__(self, books):
        self.books = books  # Lista de objetos Book

    def recommend_by_genre(self, user):
        recommendations = [book for book in self.books if book.genre in user.favorite_genres]
        return recommendations

    def recommend_by_author(self, user):
        recommendations = [book for book in self.books if book.author in user.favorite_authors]
        return recommendations
