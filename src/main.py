from ebook import Ebook
from printed_book import PrintedBook
from user import User
from recommender import BookRecommender

def main():
    books = [
        Ebook("1984", "George Orwell", "Dystopia", 4.6, 2.5),
        PrintedBook("Pride and Prejudice", "Jane Austen", "Romance", 4.3, 432),
        Ebook("Dune", "Frank Herbert", "Science Fiction", 4.5, 3.1),
        PrintedBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4.7, 310),
        PrintedBook("To Kill a Mockingbird", "Harper Lee", "Classic", 4.4, 281),
    ]

    user = User("Erika")
    user.add_genre("Dystopia")
    user.add_author("J.R.R. Tolkien")

    recommender = BookRecommender(books)

    genre_recs = recommender.recommend_by_genre(user)
    author_recs = recommender.recommend_by_author(user)

    print(f"Recomendaciones por género para {user.username}:")
    for book in genre_recs:
        print(f" - {book}")

    print(f"\nRecomendaciones por autor para {user.username}:")
    for book in author_recs:
        print(f" - {book}")

if __name__ == "__main__":
    main()
