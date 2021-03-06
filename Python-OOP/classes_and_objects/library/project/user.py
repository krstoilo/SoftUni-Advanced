class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for book in library.books_available[author]:
            if book_name == book:
                self.books.append(book_name)
                if self.username in library.rented_books:
                    library.rented_books[self.username][book_name] = days_to_return
                else:
                    library.rented_books[self.username] = {}
                    library.rented_books[self.username][book_name] = days_to_return
                library.books_available[author].remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user in library.rented_books:
            for book in library.rented_books[user]:
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {library.rented_books[user][book_name]} days!"'
        return f"No such book exists in library"

    def return_book(self, author: str, book_name: str, library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            del library.rented_books[self.username][book_name]
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        sorted_books = ", ".join(sorted(self.books))
        return sorted_books

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
