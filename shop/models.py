import uuid

from django.conf import settings
from django.db import models
from useraccount.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    currency = models.CharField(max_length=40)
    imageSrc = models.ImageField(upload_to='uploads/shops')
    imageAlt = models.CharField(max_length=155)

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.imageSrc.url}'

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='sales', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=30)
    street = models.CharField(max_length=120)
    cep = models.CharField(max_length=90)
    number = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name='sales', on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)