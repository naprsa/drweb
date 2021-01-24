from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField("Название", max_length=150)
    author = models.ForeignKey(
        "books.Author",
        verbose_name="Автор",
        on_delete=models.CASCADE,
        related_name="books",
    )

    class Meta:
        ordering = ["author", "title"]

    def __str__(self):
        return f"{self.title} [{self.author}]"


class Author(models.Model):
    full_name = models.CharField("ФИО Автора", max_length=100)

    def __str__(self):
        return self.full_name


class Shelf(models.Model):
    id = models.IntegerField("Номенр полки", primary_key=True)

    def __str__(self):
        return f"Полка №{self.id}"


class BookOnShelf(models.Model):
    book = models.OneToOneField(
        "books.Book",
        verbose_name="Книга",
        on_delete=models.CASCADE,
        default=None,
    )
    shelf = models.ForeignKey(
        "books.Shelf", on_delete=models.CASCADE, related_name="books_on_shelf"
    )
    position = models.PositiveIntegerField("Позиция на полке", null=True, blank=True)

    class Meta:
        ordering = ["shelf", "position"]

    def __str__(self):
        return f"[{self.shelf}] ({self.position}) {self.book}"

    def save(self, *args, update_fields=None, **kwargs):
        if (
            not self.position
            and self.__class__.objects.filter(shelf=self.shelf).exists()
        ):
            self.position = 1
        elif (
            not self.position
            and not update_fields
            and self.__class__.objects.filter(shelf=self.shelf).exists()
        ):
            self.position = (
                self.__class__.objects.filter(shelf=self.shelf).last().position + 1
            )

        super().save(*args, **kwargs)

    def change_position(self, to_book):
        to_book.position, self.position = self.position, to_book.position
        to_book.save(update_fields=["position"])
        self.save(update_fields=["position"])
