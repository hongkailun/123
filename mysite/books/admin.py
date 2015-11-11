
# Register your models here.
from django.contrib import admin
from books.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorID', 'Name','Age','Country')
class BookAdmin(admin.ModelAdmin):
    list_display= ('ISBN','Title','AuthorID','Publisher','PublishDate','Price')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
