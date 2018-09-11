# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class NsBlog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=20)
    bog_image = models.ImageField(null=True, blank=True, upload_to="static/upload")
    blog_desc = models.TextField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_blog'


class NsCartItems(models.Model):
    product_id = models.IntegerField()
    quantity = models.FloatField()
    product_name = models.TextField()
    product_price = models.FloatField()
    user_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_cart_items'


class NsCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    status = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_category'


class NsOptions(models.Model):
    options_id = models.AutoField(primary_key=True)
    option_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ns_options'


class NsProductColors(models.Model):
    product_color_id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    color_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ns_product_colors'


class NsProductOptions(models.Model):
    product_options_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_group_id = models.IntegerField()
    option_price_increment = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ns_product_options'


class NsProductSizes(models.Model):
    product_size_id = models.BigAutoField(primary_key=True)
    size_id = models.IntegerField()
    product_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ns_product_sizes'


class NsProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_sku = models.CharField(max_length=20)
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_weight = models.CharField(max_length=50)
    product_cart_desc = models.TextField()
    product_short_desc = models.TextField()
    product_long_desc = models.TextField()
    product_thumb = models.CharField(max_length=100)
    product_image = models.CharField(max_length=255)
    product_category_id = models.IntegerField()
    product_sub_category_id = models.IntegerField()
    product_sub_sub_category_id = models.IntegerField()
    modified_date = models.DateTimeField()
    status = models.IntegerField()
    product_stock = models.IntegerField()
    tags = models.TextField()

    class Meta:
        managed = False
        db_table = 'ns_products'


class NsSubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    sub_category_name = models.CharField(max_length=100)
    status = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_sub_category'


class NsSubSubCategory(models.Model):
    sub_sub_category_id = models.AutoField(primary_key=True)
    sub_category_id = models.IntegerField()
    category_id = models.IntegerField()
    sub_sub_category_name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_sub_sub_category'


class NsUsers(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    user_firstname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_zip = models.IntegerField(blank=True, null=True)
    user_email_auth = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    user_ip = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_address = models.TextField()
    user_country = models.CharField(max_length=50)
    user_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ns_users'


class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    url = models.TextField()
    product_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_image'
