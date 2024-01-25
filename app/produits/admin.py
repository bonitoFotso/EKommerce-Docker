from django.contrib import admin
from .models import *


class KeyModelAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'key')

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','description')

class ProduitModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory',  'price', 'digital', 'image', 'date_ajout')    

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'key', 'value')
    list_filter = ('subcategory',)
    search_fields = ('subcategory__name', 'key', 'value')

admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Key, KeyModelAdmin)
admin.site.register(Produit, ProduitModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory, SubCategoryModelAdmin)


admin.site.site_title  = "EKommerce"
admin.site.site_header = "EKommerce"
admin.site.index_title = "EKommerce"