from rest_framework import serializers

from shop.models import (Client, Category, Produit, 
                        Commande, CommandeArticle, 
                        AddressChipping, ProductAttribute, SubCategory, Key)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'name', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']

class KeySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    class Meta:
        model = Key
        fields = ['id', 'subcategory', 'key']

class ProductAttributeSerializer(serializers.ModelSerializer):
    key = KeySerializer()
    class Meta:
        model = ProductAttribute
        fields = ['key', 'value']

    def to_representation(self, instance):
        # Personnalise la représentation pour obtenir un dictionnaire clé-valeur
        return {
            instance.key.key: instance.value
        }


class ProduitSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    
    # Utilisation du ProductAttributeSerializer pour sérialiser les attributs personnalisés
    fields = ProductAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Produit
        fields = ['id', 'subcategory', 'name', 'price', 'digital', 'image', 'date_ajout', 'stock', 'fields']
        read_only_fields = ['date_ajout', 'id']

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['id', 'client', 'date_commande', 'complete', 'transaction_id', 'status', 'total_trans']


class CommandeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeArticle
        fields = ['id', 'produit', 'commande', 'quantite', 'date_added', 'get_total']


class AddressChippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressChipping
        fields = ['id', 'client', 'commande', 'addresse', 'ville', 'zipcode', 'date_ajout']


