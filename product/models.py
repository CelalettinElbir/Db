from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="products/images")
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey(
        'self', models.CASCADE, null=True, blank=True, related_name="chileren")

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        managed = False
        db_table = 'product_category'





class ProductItem(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    sku = models.CharField(max_length=45, blank=True, null=True)
    in_stock = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_image = models.ImageField(blank=True, upload_to="item/images")

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        managed = False
        db_table = 'product_item'
        unique_together = (('id', 'product'),)


class Variation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = 'variation'
        unique_together = (('id', 'product_category'),)


class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, models.DO_NOTHING)
    value = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation_option'


class ProductConfigiraton(models.Model):
    # id = models.AutoField(primary_key=true)
    variation_option = models.ForeignKey(VariationOption, models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_configiraton'