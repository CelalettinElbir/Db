from django.db import models
from mptt.models import MPTTModel
from django.urls import reverse
from mptt.fields import TreeForeignKey
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to="products/images")
    product_category = models.ForeignKey('Category', models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    def get_product_ıtem(self):
        return Item.objects.get(pk=self.id)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)



# product category tabe
class Category(MPTTModel):
    category_name = models.CharField(max_length=45, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    slug = models.SlugField(null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def get_products(self):
        return Product.objects.filter(product_category=self.category_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        # post.  use __unicode__ in place of
        full_path = [self.category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' / '.join(full_path[::-1])


# categoryItem table
class Item(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    sku = models.CharField(max_length=45, blank=True, null=True)
    in_stock = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_image = models.ImageField(blank=True, upload_to="item/images")

    def __str__(self) -> str:
        return self.product.name


# variation table
class Variation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey(Category, models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


#  variationOption table
class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, models.DO_NOTHING)
    value = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.value


# ProductConfigiration table
class Configiraton(models.Model):
    int = models.AutoField(primary_key=True)
    variation_option = models.ForeignKey('VariationOption', models.DO_NOTHING)
    product_item = models.ForeignKey('Item', models.DO_NOTHING)


# class ProductCategory(MPTTModel):
#     category_name = models.CharField(max_length=45, blank=True, null=True)
#     Product_category = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)


#     def __str__(self) -> str:
#         return self.category_name

#     class Meta:
#         managed = False
#         db_table = 'product_category'
