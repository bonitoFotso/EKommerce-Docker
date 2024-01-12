from django.contrib import admin
from .models import *


#@admin.register(Clothing)
#class ClothingAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price', 'stock_quantity', 'color', 'size', 'brand')
#
#@admin.register(HardDrive)
#class HardDriveAdmin(admin.ModelAdmin):
#    list_display = ('name', 'price', 'stock_quantity', 'type', 'capacity')


class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')

class KeyModelAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'key')

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','description')

class ProduitModelAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'name', 'price', 'digital', 'image', 'date_ajout')    

class CommandeModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'complete', 'status', 'total_trans', 'transaction_id', 'date_commande')    

class CommandeArticleModelAdmin(admin.ModelAdmin):
    list_display = ('produit', 'commande', 'quantite', 'date_added')  

class AddressChippingModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'commande', 'addresse', 'ville', 'zipcode', 'date_ajout')      

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'key', 'value')
    list_filter = ('subcategory',)
    search_fields = ('subcategory__name', 'key', 'value')

admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Client, ClientModelAdmin)
admin.site.register(Key, KeyModelAdmin)
admin.site.register(Produit, ProduitModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory, SubCategoryModelAdmin)
admin.site.register(Commande, CommandeModelAdmin)
admin.site.register(CommandeArticle, CommandeArticleModelAdmin)
admin.site.register(AddressChipping, AddressChippingModelAdmin)

admin.site.site_title  = "EKommerce"
admin.site.site_header = "EKommerce"
admin.site.index_title = "EKommerce"