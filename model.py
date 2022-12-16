# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    street_number = models.CharField(max_length=45, blank=True, null=True)
    adress_line = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=45, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    country_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Favorite(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    product_item = models.ForeignKey('ProductItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('id', 'user', 'product_item'),)


class OrderLine(models.Model):
    shop_order = models.ForeignKey('ShopOrder', models.DO_NOTHING)
    product_item = models.ForeignKey('ProductItem', models.DO_NOTHING)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_line'
        unique_together = (('id', 'shop_order', 'product_item'),)


class OrderStatus(models.Model):
    shop_order = models.ForeignKey('ShopOrder', models.DO_NOTHING)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status'
        unique_together = (('id', 'shop_order'),)


class Product(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    product_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductConfigiraton(models.Model):
    int = models.AutoField(primary_key=True)
    variation_option = models.ForeignKey('VariationOption', models.DO_NOTHING)
    product_item = models.ForeignKey('ProductItem', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_configiraton'


class ProductItem(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    sku = models.CharField(max_length=45, blank=True, null=True)
    in_stock = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    product_image = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_item'
        unique_together = (('id', 'product'),)


class ShopOrder(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_date = models.DateField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    order_total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'
        unique_together = (('id', 'user', 'address'),)


class ShoppingCard(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shopping_card'
        unique_together = (('id', 'user'),)


class ShoppingCardItem(models.Model):
    shopping_card = models.ForeignKey(ShoppingCard, models.DO_NOTHING)
    product_item = models.ForeignKey(ProductItem, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_card_item'
        unique_together = (('id', 'shopping_card', 'product_item'),)


class User(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    email_adress = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    comment_point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAddress(models.Model):
    is_default = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_address'


class UserPaymentMethod(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    provider = models.CharField(max_length=45, blank=True, null=True)
    account_number = models.CharField(max_length=45, blank=True, null=True)
    expiry_date = models.CharField(max_length=45, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_payment_method'
        unique_together = (('id', 'user'),)


class UserReview(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    rating_value = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    order_line_product_item = models.ForeignKey(OrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_review'
        unique_together = (('id', 'user', 'order_line_product_item'),)


class Variation(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

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
