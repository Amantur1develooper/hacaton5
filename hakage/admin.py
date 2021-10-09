from django.contrib import admin
from .models import products,Category 
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'title', 'photo','category']
admin.site.register(products,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)