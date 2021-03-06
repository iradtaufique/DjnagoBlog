from django.contrib import admin
from .models import Board, Topic, Post

# Register your models here.
admin.site.site_header ="Taufique"
class admin_board(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)

admin.site.register(Board, admin_board)
admin.site.register(Post)
admin.site.register(Topic)
