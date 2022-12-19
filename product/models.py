from django.db import models
from mptt.models import MPTTModel
from django.urls import reverse
from mptt.fields import TreeForeignKey
from django.utils.text import slugify
from django.db.models import Min
import random

class Product(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="products/images")
    product_category = models.ForeignKey('Category', models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    def get_product_items(self):
        return Item.objects.filter(product=self.id)

    def get_min_price(self):
        return Item.objects.filter(product=self.id).aggregate(Min('price'))

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
    slug = models.SlugField(null=True, blank=True)
    product_image = models.ImageField(blank=True, upload_to="item/images")
    variations = models.ManyToManyField("VariationOption")

    def __str__(self) -> str:
        return self.product.name

    def get_absolute_url(self):
        return reverse('Item', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # self.sku = self.product.name[0:2] + self.product.product_category.name[0:2]+random.randint(0,1000)
        self.slug = slugify(self.product.name )
        super(Item, self).save(*args, **kwargs)

    def product_detail(self):
        return Product.objects.get(pk=self.id)

    # def product_configirations(self):
    #     return Configiraton.objects.filter(product_item = self.id)


# variation table
class Variation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey(Category, models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    def get_variation_options(self):
        return VariationOption.objects.filter(variation_id=self.id)


#  variationOption table
class VariationOption(models.Model):
    variation_id = models.ForeignKey(Variation, models.DO_NOTHING)
    value = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self) -> str:
        return self.value


# ProductConfigiration table
# class Configiraton(models.Model):
#     int = models.AutoField(primary_key=True)
#     variation_option = models.ForeignKey('VariationOption', models.DO_NOTHING)
#     product_item = models.ForeignKey('Item', models.DO_NOTHING)

#     #foregin keyler sayersinde direkt olarak diğer tabloya ulaşabiliyoruz!!11
#     def __str__(self):
#         return  str(self.int ) +  self.variation_option.value

#     def get_variation_option(self):
#         return VariationOption.objects.filter(id = self.variation_option)
