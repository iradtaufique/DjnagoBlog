from django.contrib import admin
from .models import Board

# Register your models here.
class admin_board(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)

admin.site.register(Board, admin_board)
