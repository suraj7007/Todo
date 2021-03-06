from django.contrib import admin
from .models import TODO

# Register your models here.
@admin.register(TODO)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status', 'date', 'priority']