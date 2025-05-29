from book import Book
from user import User
from recommender import BookRecommender
from services.filters import filter_by_genre, get_average_rating, get_titles

def main():
    books = [
        Book("1984", "George Orwell", "Dystopia", 4.6),
        Book("Pride and Prejudice", "Jane Austen", "Romance", 4.3),
        Book("Dune", "Frank Herbert", "Science Fiction", 4.5),
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4.7),
        Book("To Kill a Mockingbird", "Harper Lee", "Classic", 4.4),
    ]

    dystopia_books = filter_by_genre(books, "Dystopia")
    titles = get_titles(dystopia_books)
    avg_rating = get_average_rating(dystopia_books)

    print("Libros de género Dystopia:")
    for title in titles:
        print(f" - {title}")

    print(f"Calificación promedio: {avg_rating:.2f}")

if __name__ == "__main__":
    main()
