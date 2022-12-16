from django.contrib import admin
from .models import *
# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from mptt.admin import MPTTModelAdmin

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status','image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    # inlines = [ProductImageInline,ProductVariantsInline,ProductLangInline]


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "category_name"
    list_display = ('tree_actions', 'category_name',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'categories',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "product_category"]


class ProductCategoryAdmin(MPTTModelAdmin):
    # list_display = ["id", "product_category", "category_name"]
    # list_editable = ('category_name',)
    mptt_level_indent = 20


class ProductConfigiratonAdmin(admin.ModelAdmin):
    list_display = ["product_item"]
    fields = ('product_item')


class ProductItemAdmin(admin.ModelAdmin):
    list_display = ["product", "sku", "in_stock", "price", "product_image"]


class VariationAdmin(admin.ModelAdmin):
    list_display = ["name", "product_category"]


class variationOptionAdmin(admin.ModelAdmin):
    list_display = ["variation", "value"]


admin.site.register(Product, CategoryAdmin)

# admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(Configiraton)

admin.site.register(Item, ProductItemAdmin)

admin.site.register(VariationOption, variationOptionAdmin)

admin.site.register(Variation, VariationAdmin)

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
