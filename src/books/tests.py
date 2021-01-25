from django.test import TestCase
import factory
from books.models import Book, Author, BookOnShelf, Shelf


class AuthorFactory(factory.DjangoModelFactory):
    full_name = factory.Faker("name")

    class Meta:
        model = Author


class BookFactory(factory.DjangoModelFactory):
    title = factory.Faker("sentence", nb_words=2, locale="ru_RU")
    author = factory.SubFactory(AuthorFactory)

    class Meta:
        model = Book


class ShelfFactory(factory.DjangoModelFactory):
    id = factory.Faker("pyint")

    class Meta:
        model = Shelf


class BookOnShelfFactory(factory.DjangoModelFactory):
    book = factory.SubFactory(BookFactory)
    shelf = factory.SubFactory(ShelfFactory)
    position = factory.Sequence(lambda n: n)

    class Meta:
        model = BookOnShelf


class BookOnShelfTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        pass

    def test_book_on_shelf_change_position(self):
        pass
