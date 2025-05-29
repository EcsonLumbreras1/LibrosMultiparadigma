import csv
from book import Book

def load_books_from_csv(path):
    books = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertir rating a float
            rating = float(row['rating']) if row['rating'] else 0.0
            book = Book(
                title=row['title'],
                author=row['author'],
                genre=row['genre'],
                rating=rating
            )
            books.append(book)
    return books
