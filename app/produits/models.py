from django.db import models


from django.utils import timezone
#1
from clients.models import Client

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    
class Key(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subcategory.name} - {self.key}"

    

class ProductAttribute(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subcategory.name} - {self.key}: {self.value}"

class Produit(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_ajout = models.DateTimeField(default=timezone.now)
    stock = models.IntegerField()
    
    # Utilisation d'une relation many-to-many avec ProductAttribute
    fields = models.ManyToManyField(ProductAttribute, blank=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.name} ({self.price} XAF)"

    def get_image_url(self):
        return self.image.url if self.image else ''
           


