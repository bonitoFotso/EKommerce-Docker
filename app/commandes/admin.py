from django.contrib import admin
from .models import *


class CommandeModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'complete', 'status', 'total_trans', 'transaction_id', 'date_commande')    

class CommandeArticleModelAdmin(admin.ModelAdmin):
    list_display = ('produit', 'commande', 'quantite', 'date_added')  

class AddressChippingModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'commande', 'addresse', 'ville', 'zipcode', 'date_ajout')      


admin.site.register(Commande, CommandeModelAdmin)
admin.site.register(CommandeArticle, CommandeArticleModelAdmin)
admin.site.register(AddressChipping, AddressChippingModelAdmin)