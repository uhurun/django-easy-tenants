import uuid

from django.db import models
from easy_tenants.models import TenantMixin, TenantAbstract
from easy_tenants.managers import TenantManager


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Customer(TenantMixin, BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(TenantAbstract, BaseModel):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('app_test.Category', on_delete=models.CASCADE)

    objects = TenantManager()

    def __str__(self):
        return self.name


class Category(TenantAbstract, BaseModel):
    name = models.CharField(max_length=50)

    objects = TenantManager()

    def __str__(self):
        return self.name
