from django.contrib import admin

from books.models import Author, Book, BookOnShelf, Shelf

# Register your models here.

admin.site.register(Book)
admin.site.register(Shelf)
admin.site.register(BookOnShelf)
admin.site.register(Author)
