from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.shortcuts import render

from books.models import Author, Book, BookOnShelf, Shelf


def index(request):
    template = "index.html"
    context = {"books": Book.objects.all().select_related("author")}
    return render(request, template, context)


class AuthorListView(ListView):
    model = Author
    template_name = "list.html"


class BookListView(ListView):
    model = Book
    template_name = "list.html"

    def get_queryset(self, **kwargs):
        author_id = self.kwargs.get("author_id")
        if author_id:
            return super().get_queryset().filter(author_id=author_id)
        return super().get_queryset()


class BooksOnShelfListView(ListView):
    model = BookOnShelf
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shelfs"] = Shelf.objects.all()
        return context


class BookUpdateView(UpdateView):
    model = BookOnShelf
    template_name = "update_book.html"
