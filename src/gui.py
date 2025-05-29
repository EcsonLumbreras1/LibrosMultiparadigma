import tkinter as tk
from tkinter import ttk, messagebox
from user import User
from recommender import BookRecommender
from loader import load_books_from_csv
import threading

class BookRecommenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Recomendador de Libros")
        self.root.geometry("520x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")  # Fondo claro suave
        # Ícono (opcional), pon la ruta de tu ícono .ico si tienes
        # self.root.iconbitmap('path_to_icon.ico')

        # Estilos personalizados
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#0052cc')
        style.configure('TLabel', background="#f0f4f8", font=('Helvetica', 11))
        style.configure('Header.TLabel', font=('Helvetica', 18, 'bold'), background="#f0f4f8", foreground='#003366')

        # Cargar libros
        self.books = load_books_from_csv('../data/books.csv')
        self.recommender = BookRecommender(self.books)
        self.user = User("Usuario")

        # Título
        title_label = ttk.Label(root, text="Recomendador de Libros", style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=15)

        # Widgets
        ttk.Label(root, text="Ingrese género favorito:").grid(row=1, column=0, padx=10, pady=6, sticky="e")
        self.genre_entry = ttk.Entry(root, font=('Helvetica', 11))
        self.genre_entry.grid(row=1, column=1, padx=10, pady=6)
        self.genre_entry.bind("<KeyRelease>", self.check_entries)

        ttk.Label(root, text="Ingrese autor favorito:").grid(row=2, column=0, padx=10, pady=6, sticky="e")
        self.author_entry = ttk.Entry(root, font=('Helvetica', 11))
        self.author_entry.grid(row=2, column=1, padx=10, pady=6)
        self.author_entry.bind("<KeyRelease>", self.check_entries)

        self.search_btn = ttk.Button(root, text="Buscar recomendaciones", command=self.search, state="disabled", cursor="hand2")
        self.search_btn.grid(row=3, column=0, columnspan=2, pady=12)

        ttk.Separator(root, orient='horizontal').grid(row=4, column=0, columnspan=2, sticky="ew", pady=8)

        self.status_label = ttk.Label(root, text="", foreground="green", background="#f0f4f8")
        self.status_label.grid(row=5, column=0, columnspan=2)

        self.result_text = tk.Text(root, width=62, height=15, state="disabled", relief='groove', bd=3, font=('Consolas', 11))
        self.result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def check_entries(self, event=None):
        genre = self.genre_entry.get().strip()
        author = self.author_entry.get().strip()
        if genre or author:
            self.search_btn.config(state="normal")
        else:
            self.search_btn.config(state="disabled")

    def search(self):
        self.search_btn.config(state="disabled")
        self.status_label.config(text="Buscando recomendaciones...")
        threading.Thread(target=self.perform_search).start()

    def perform_search(self):
        genre = self.genre_entry.get().strip()
        author = self.author_entry.get().strip()

        self.user.favorite_genres = [genre] if genre else []
        self.user.favorite_authors = [author] if author else []

        genre_recs = self.recommender.recommend_by_genre(self.user)
        author_recs = self.recommender.recommend_by_author(self.user)

        results = ""
        if genre_recs:
            results += f"Recomendaciones por género '{genre}':\n"
            for book in genre_recs:
                results += f"- {book}\n"
            results += "\n"
        if author_recs:
            results += f"Recomendaciones por autor '{author}':\n"
            for book in author_recs:
                results += f"- {book}\n"

        if not genre_recs and not author_recs:
            results = "No se encontraron recomendaciones."

        self.result_text.after(0, self.update_results, results)

    def update_results(self, text):
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state="disabled")
        self.status_label.config(text="")
        self.check_entries()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookRecommenderGUI(root)
    root.mainloop()
