from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "product_category"]

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "product_category", "category_name"]

class ProductConfigiratonAdmin(admin.ModelAdmin):
    list_display = ["id","variation_option", "product_item"]

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ["product", "sku", "in_stock", "price", "product_image"]

class VariationAdmin(admin.ModelAdmin):
    list_display = ["name", "product_category"]

class variationOptionAdmin(admin.ModelAdmin):
    list_display = ["variation", "value"]


admin.site.register(Product, CategoryAdmin)

admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductConfigiraton, ProductConfigiratonAdmin)

admin.site.register(ProductItem, ProductItemAdmin)

admin.site.register(VariationOption, variationOptionAdmin)

admin.site.register(Variation, VariationAdmin)
