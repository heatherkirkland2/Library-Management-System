class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True

    # Getters and setters for encapsulation
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def availability(self):
        return self.__availability

    def borrow(self):
        self.__availability = False

    def return_book(self):
        self.__availability = True

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and setters for encapsulation
    @property
    def name(self):
        return self.__name

    @property
    def library_id(self):
        return self.__library_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.availability:
            self.__borrowed_books.append(book)
            book.borrow()
        else:
            print("Book is not available")

    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
        else:
            print("User has not borrowed this book")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and setters for encapsulation
    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

def book_operations(books, users):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date: ")
            book = Book(title, author, genre, publication_date)
            books.append(book)
            print("Book added successfully!")
        elif choice == "2":
            title = input("Enter book title to borrow: ")
            book = next((b for b in books if b.title == title), None)
            if book:
                user_id = int(input("Enter user ID: "))
                user = next((u for u in users if u.library_id == user_id), None)
                if user:
                    user.borrow_book(book)
                    print("Book borrowed successfully!")
                else:
                    print("User not found")
            else:
                print("Book not found")
        elif choice == "3":
            title = input("Enter book title to return: ")
            book = next((b for b in books if b.title == title), None)
            if book:
                user_id = int(input("Enter user ID: "))
                user = next((u for u in users if u.library_id == user_id), None)
                if user:
                    user.return_book(book)
                    print("Book returned successfully!")
                else:
                    print("User not found")
            else:
                print("Book not found")
        elif choice == "4":
            title = input("Enter book title to search: ")
            book = next((b for b in books if b.title == title), None)
            if book:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Genre: {book.genre}")
                print(f"Publication Date: {book.publication_date}")
                print(f"Availability: {'Available' if book.availability else 'Borrowed'}")
            else:
                print("Book not found")
        elif choice == "5":
            for book in books:
                print(f"Title: {book.title}, Availability: {'Available' if book.availability else 'Borrowed'}")
        elif choice == "6":
            break
        else:
            print("Invalid choice")

def user_operations(users):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter user name: ")
            library_id = int(input("Enter library ID: "))
            user = User(name, library_id)
            users.append(user)
            print("User added successfully!")
        elif choice == "2":
            library_id = int(input("Enter library ID: "))
            user = next((u for u in users if u.library_id == library_id), None)
            if user:
                print(f"Name: {user.name}")
                print(f"Library ID: {user.library_id}")
                print("Borrowed Books:")
                for book in user.borrowed_books:
                    print(f"- {book.title}")
            else:
                print("User not found")
        elif choice == "3":
            for user in users:
                print(f"Name: {user.name}, Library ID: {user.library_id}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def author_operations(authors):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            authors.append(author)
            print("Author added successfully!")
        elif choice == "2":
            name = input("Enter author name: ")
            author = next((a for a in authors if a.name == name), None)
            if author:
                print(f"Name: {author.name}")
                print(f"Biography: {author.biography}")
            else:
                print("Author not found")
        elif choice == "3":
            for author in authors:
                print(f"Name: {author.name}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def main():
    books = []
    users = []
    authors = []

    while True:
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_operations(books, users)
        elif choice == "2":
            user_operations(users)
        elif choice == "3":
            author_operations(authors)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

