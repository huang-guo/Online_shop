from django.db import models

# Create your models here.
from .fields import ImmutableCharField


class Classification(models.Model):
    id = ImmutableCharField(max_length=5, primary_key=True, verbose_name="分类编码")
    tax_classification_code = ImmutableCharField(max_length=19, verbose_name='税收分类编码')
    classification = models.CharField(max_length=10, verbose_name="分类", unique=True)
    tax = models.FloatField(verbose_name="税率")

    def __str__(self):
        return self.classification


class Commodity(models.Model):
    id = ImmutableCharField(
        max_length=8, verbose_name="编码", primary_key=True)
    brand = models.CharField(max_length=10, verbose_name="品牌")
    model_number = models.CharField(max_length=20, verbose_name="型号")
    specifications = models.CharField(max_length=20, verbose_name="规格")
    classification = models.ForeignKey(
        Classification, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model_number}' \
               f' {self.classification} {self.specifications}'


class Barcode(models.Model):
    unit = models.CharField(max_length=10, verbose_name="单位")
    relationship = models.FloatField(verbose_name="单位关系")
    barcode = models.CharField(max_length=20)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name="商品")
    price1 = models.FloatField(verbose_name="预设售价1", default=0)
    price2 = models.FloatField(verbose_name="预设售价2", default=0)
    price3 = models.FloatField(verbose_name="预设售价3", default=0)
