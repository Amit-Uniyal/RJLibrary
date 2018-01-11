from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Author


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors
        }
    )

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('index')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('index')


# def addBook(request):
#     authors = Author.objects.all()
#     books = Book.objects.all()
#
#     return render(
#         request,
#         'add_book.html',
#         context={
#             'authors': authors,
#             'books': books,
#         }
#     )

def listBooks(request):
    book_list = Book.objects.all()
    return render(
        request,
        'book_list.html',
        context={
            'books': book_list
        }
    )


def bookDetails(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    return render(
        request,
        'book_detail.html',
        context={'book': book_id, }
    )

def listAuthors(request):
    author_list = Author.objects.all()
    return render(
        request,
        'author_list.html',
        context={
            'authors': author_list
        }
    )

