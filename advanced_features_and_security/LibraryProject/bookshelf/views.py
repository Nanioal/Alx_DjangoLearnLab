from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author_id = request.POST['author_id']
        publication_year = request.POST['publication_year']
        Book.objects.create(title=title, author_id=author_id, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author_id = request.POST['author_id']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

# Create your views here.
