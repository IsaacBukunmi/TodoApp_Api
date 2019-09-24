from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo_subject', 'check')
    list_display_links = ('id', 'todo_subject')
    search_fields = ('todo_subject', 'todo_details')
    list_per_page = 25

admin.site.register(Todo, TodoAdmin)
