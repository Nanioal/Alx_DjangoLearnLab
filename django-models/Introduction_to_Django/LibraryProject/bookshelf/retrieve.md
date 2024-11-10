# Retrieve a Book Instance

```python
book = Book.objects.get(title="1984")
print(book)
# Output: 1984
print(book.author)
# Output: George Orwell
print(book.publication_year)
# Output: 1949

#### Update the Book Title
```python
book.title = "Nineteen Eighty-Four"
book.save()