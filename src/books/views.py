from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.urls import reverse

from books.forms import BookOnShelfForm
from books.models import Author, Book, BookOnShelf, Shelf


def index(request):
    template = "index.html"
    context = {"books": Book.objects.all().select_related("author")}
    context["shelfs"] = Shelf.objects.all()
    return render(request, template, context)


class AuthorListView(ListView):
    model = Author
    template_name = "authors.html"


class BookListView(ListView):
    model = Book
    template_name = "books_by_author_list.html"

    def get_queryset(self, **kwargs):
        author_id = self.kwargs.get("author_id")
        if author_id:
            return super().get_queryset().filter(author_id=author_id)
        return super().get_queryset()


@method_decorator(never_cache, name="dispatch")
class BooksOnShelfListView(ListView):
    model = BookOnShelf
    template_name = "books_on_shelf_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shelfs"] = Shelf.objects.all()
        return context

    def get_queryset(self):
        shelf_id = self.kwargs.get("shelf_id")
        if shelf_id:
            return super().get_queryset().filter(shelf_id=shelf_id)
        return super().get_queryset()


class BookUpdateView(UpdateView):
    model = BookOnShelf
    form_class = BookOnShelfForm
    template_name = "update_book.html"

    def get_success_url(self):
        shelf_id = self.get_object().shelf.pk
        url = reverse("books:books_on_shelf", kwargs={"shelf_id": shelf_id})
        return url
