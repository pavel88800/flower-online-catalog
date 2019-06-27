from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,)

    def __str__(self):
        return self.title
