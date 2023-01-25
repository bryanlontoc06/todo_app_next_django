from django.contrib import admin
from .models import Todo, Author

class TodoModelAdmin(admin.ModelAdmin):
    list_display=('description', 'author', 'completed')
    search_fields=('description', 'author__authorName')
    list_per_page = 10

class AuthorModelAdmin(admin.ModelAdmin):
    list_per_page = 10

# Register your models here.

admin.site.register(Todo, TodoModelAdmin)
admin.site.register(Author, AuthorModelAdmin)