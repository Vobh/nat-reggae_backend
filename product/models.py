import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.IntegerField()
    days = models.IntegerField()
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    #favorited
    image = models.ImageField(upload_to='uploads/products')
    vendor = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'