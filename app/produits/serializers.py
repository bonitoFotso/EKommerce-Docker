# serializers.py

from rest_framework import serializers
from .models import ( Produit, ProductAttribute, 
                        Key,Category,SubCategory )


from rest_framework import serializers

class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SubCategoryDisplaySerializer(serializers.ModelSerializer):
    category = CategoryCreateUpdateSerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name','category', 'description']



class CategoryDisplaySerializer(serializers.ModelSerializer):
    subcategories = SubCategoryDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories']


        
class SubCategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name','category', 'description']
class KeyDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['id', 'key']

class KeyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ['key']

class ProductAttributeDisplaySerializer(serializers.ModelSerializer):
    key = KeyDisplaySerializer()

    class Meta:
        model = ProductAttribute
        fields = ['key', 'value']

    def to_representation(self, instance):
        # Personnalise la représentation pour obtenir un dictionnaire clé-valeur
        return {
            instance.key.key: instance.value
        }

class ProductAttributeCreateSerializer(serializers.ModelSerializer):
    key = KeyCreateSerializer()

    class Meta:
        model = ProductAttribute
        fields = ['key', 'value']

class ProduitDisplaySerializer(serializers.ModelSerializer):
    subcategory = SubCategoryDisplaySerializer(read_only=True)
    fields = ProductAttributeDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Produit
        fields = ['id', 'subcategory', 'name', 'price', 'digital', 'image', 'date_ajout', 'stock', 'fields']
        read_only_fields = ['date_ajout', 'id']
class ProduitCreateUpdateSerializer(serializers.ModelSerializer):
    #fields = ProductAttributeCreateSerializer(many=True,)

    class Meta:
        model = Produit
        fields = ['name', 'price', 'digital', 'image', 'stock', 'fields']

