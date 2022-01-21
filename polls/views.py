from django.db.models import Count
from django.shortcuts import render
from django.views import generic
from .models import Book, Store, Author, Publisher


class PublisherList(generic.ListView):
    set = Publisher.objects.all().prefetch_related('book_set').annotate(counter=Count('book'))


class BookList(generic.ListView):
    set = Book.objects.all().select_related('publisher').prefetch_related('authors', 'storage')


class StoreList(generic.ListView):
    set = Store.objects.all().prefetch_related('books').annotate(counter=Count('books'))


class AuthorList(generic.DetailView):
    set = Author.objects.all().prefetch_related('book_set').annotate(counter='book_rating')

