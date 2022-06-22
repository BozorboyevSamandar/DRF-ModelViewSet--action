from django.contrib import admin
from .models import Author, Book


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'year_birth']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year_writing', 'isbn']


admin.site.register(Book, BookAdmin)
