import tkinter as tk
from tkinter import messagebox
from movies_data import CineMatch

class CineMatchGUI:
    def __init__(self, root):
        self.cinematch = CineMatch()
        self.root = root
        self.root.title("CineMatch")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Add movie section
        tk.Label(self.root, text="Add Movie").grid(row=0, column=0, pady=10)
        
        tk.Label(self.root, text="Title:").grid(row=1, column=0)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Genre:").grid(row=2, column=0)
        self.genre_entry = tk.Entry(self.root)
        self.genre_entry.grid(row=2, column=1)
        
        self.add_button = tk.Button(self.root, text="Add Movie", command=self.add_movie)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Search movie section
        tk.Label(self.root, text="Search Movie").grid(row=4, column=0, pady=10)
        
        tk.Label(self.root, text="Query:").grid(row=5, column=0)
        self.search_query_entry = tk.Entry(self.root)
        self.search_query_entry.grid(row=5, column=1)
        
        self.search_type = tk.StringVar(value="title")
        tk.Radiobutton(self.root, text="Title", variable=self.search_type, value="title").grid(row=6, column=0)
        tk.Radiobutton(self.root, text="Genre", variable=self.search_type, value="genre").grid(row=6, column=1)
        
        self.search_button = tk.Button(self.root, text="Search", command=self.search_movie)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.search_results = tk.Text(self.root, height=10, width=50)
        self.search_results.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Recommend movie section
        tk.Label(self.root, text="Recommend Top  Movies").grid(row=9, column=0, pady=10)
        
        tk.Label(self.root, text="N:").grid(row=10, column=0)
        self.top_n_entry = tk.Entry(self.root)
        self.top_n_entry.grid(row=10, column=1)
        
        self.recommend_button = tk.Button(self.root, text="Recommend", command=self.recommend_movies)
        self.recommend_button.grid(row=11, column=0, columnspan=2, pady=10)
        
        self.recommendations = tk.Text(self.root, height=10, width=50)
        self.recommendations.grid(row=12, column=0, columnspan=2, pady=10)
        
        # Delete movie section
        tk.Label(self.root, text="Delete Movie").grid(row=13, column=0, pady=10)
        
        tk.Label(self.root, text="Title:").grid(row=14, column=0)
        self.delete_title_entry = tk.Entry(self.root)
        self.delete_title_entry.grid(row=14, column=1)
        
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_movie)
        self.delete_button.grid(row=15, column=0, columnspan=2, pady=10)
    
    def add_movie(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        self.cinematch.add_movie(title, genre)
        messagebox.showinfo("Success", "Movie added successfully!")
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
    
    def search_movie(self):
        query = self.search_query_entry.get()
        search_type = self.search_type.get()
        if search_type == "title":
            results = self.cinematch.search_by_title(query)
        else:
            results = self.cinematch.search_by_genre(query)
        
        self.search_results.delete(1.0, tk.END)
        if results:
            for movie in results:
                self.search_results.insert(tk.END, f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}\n")
        else:
            self.search_results.insert(tk.END, "No movies found.\n")
    
    def recommend_movies(self):
        n = int(self.top_n_entry.get())
        recommendations = self.cinematch.recommend_top_n(n)
        
        self.recommendations.delete(1.0, tk.END)
        if recommendations:
            for movie in recommendations:
                self.recommendations.insert(tk.END, f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}\n")
        else:
            self.recommendations.insert(tk.END, "No movies available for recommendation.\n")
    
    def delete_movie(self):
        title = self.delete_title_entry.get()
        self.cinematch.delete_movie(title)
        messagebox.showinfo("Success", "Movie deleted successfully!")
        self.delete_title_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CineMatchGUI(root)
    root.mainloop()
