from django.contrib import admin
from .models import Blog
 
@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    
    list_display =('author','name', 'topics','pub_date') 
    list_filter = ('pub_date',)
    search_fields = ('topics','name')
    class Meta:
        model = Blog
    