from django.urls import path

from books.views import (
    AuthorListView,
    BookListView,
    BookUpdateView,
    BooksOnShelfListView,
    index,
)


app_name = "books"

urlpatterns = [
    path("", index, name="index"),
    path("authors", AuthorListView.as_view(), name="list_authors"),
    path("author_books/<int:author_id>/", BookListView.as_view(), name="author_books"),
    path("shelfs", BooksOnShelfListView.as_view(), name="shelfs"),
    path(
        "shelfs/<int:shelf_id>", BooksOnShelfListView.as_view(), name="books_on_shelf"
    ),
    path("edit_book/<int:book_id>/", BookUpdateView.as_view(), name="edit_book"),
]
