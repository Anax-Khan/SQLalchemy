from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Set up the SQLite database
engine = create_engine('sqlite:///library.db', echo=False)
Base = declarative_base()

# Define Book table
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Set up session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    print("✅ Book added successfully!\n")

# Function to show all books
def view_books():
    books = session.query(Book).all()
    if not books:
        print("📭 No books found.\n")
    else:
        for book in books:
            print(f"{book.id}. {book.title} by {book.author}")
        print()

# Function to delete a book
def delete_book():
    view_books()
    book_id = input("Enter the ID of the book to delete: ")
    book = session.query(Book).get(int(book_id))
    if book:
        session.delete(book)
        session.commit()
        print("🗑️ Book deleted.\n")
    else:
        print("❌ Book not found.\n")

# Menu loop
def menu():
    while True:
        print("📚 Library Menu")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Delete Book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❗Invalid choice. Try again.\n")

# Run the menu
menu()
