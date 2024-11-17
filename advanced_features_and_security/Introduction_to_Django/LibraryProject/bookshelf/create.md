# Create a Book Instance

```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
# Output: <Book: 1984>

#### Retrieve the Book
```python
book = Book.objects.create(title="1984")
print(book)
print(book.author)
print(book.publication_year)