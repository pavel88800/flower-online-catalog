from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True)
    prev_img = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True, blank=True)
    date_create = models.DateField(auto_now=True)
    share = models.BooleanField(default=False, blank=True)
    new = models.BooleanField(default=False, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    img = models.ImageField(blank=True)
