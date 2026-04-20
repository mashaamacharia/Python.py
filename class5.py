class Book:
    def __init__(self, title, pages):
        self.title=title
        self.pages=pages
    
    def __len__(self):
        return self.pages

    def __str__(self):
        return self.title
    
    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Python Programming",420)
book2 = Book("Data Science",420)

print(len(book1))
print(str(book1))
print(len(book2))
print(str(book2))
print(book1 == book2)