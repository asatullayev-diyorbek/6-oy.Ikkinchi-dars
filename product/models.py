from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=25)
    size = models.IntegerField(default=1)
    count = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product/images/')

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return str(self.title)
