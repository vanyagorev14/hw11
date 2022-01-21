from django.contrib import admin
from django.db.models import Avg

from .models import Author, Book, Publisher, Store


admin.site.site_header = 'Work eleven'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'books_count']
    search = ['name']
    filter = ['age']
    fields = ['name', 'age', 'show_books']
    sort = ['age', 'books_count']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'books_count']
    search = ['name']
    fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'publisher', 'pubdate']
    search = ['name', 'publisher']
    fields = ['name', 'pages', 'publisher', 'pubdate', 'show_author']
    sort = ['pages', 'rating', 'price', 'pubdate']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'books_count', 'avg_price']
    search_fields = ['name']
