from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("ratings")) #rating__avg

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    # try:
    #   book = Book.objects.get(pk=id) # pk means primary key
    # except:
    #   raise Http404()
    # do above or below (both equivalent)
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
      "title": book.title,
      "author": book.author,
      "ratings": book.ratings,
      "is_bestselling": book.is_bestselling,
    })