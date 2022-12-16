# Generated by Django 3.2.16 on 2022-12-13 12:02

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=45, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='VariationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=45, null=True)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.variation')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products/images')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=45, null=True)),
                ('in_stock', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, upload_to='item/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Configiraton',
            fields=[
                ('int', models.AutoField(primary_key=True, serialize=False)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.item')),
                ('variation_option', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.variationoption')),
            ],
        ),
    ]