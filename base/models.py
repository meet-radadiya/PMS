from django.db import models


# Create your models here.
class CategoryVO(models.Model):
    category_id = models.AutoField(db_column="category_id", primary_key=True, null=False)
    category_name = models.CharField(db_column="category_name", max_length=255, default="", null=False)
    category_description = models.TextField(db_column="category_description", max_length=255, default="", null=False)

    def __str__(self):
        return '{} {}'.format(self.category_name, self.category_description)

    def __as_dict__(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_description': self.category_description,
        }

    class Meta:
        db_table = 'category_table'


class SubCategoryVO(models.Model):
    sub_category_id = models.AutoField(db_column="sub_category_id", primary_key=True, null=False)
    sub_category_name = models.CharField(db_column="sub_category_name", max_length=255, default="", null=False)
    sub_category_description = models.TextField(db_column="sub_category_description", max_length=255, null=False)
    sub_category_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE,
                                                 db_column='sub_category_category_id')

    def __str__(self):
        return '{} {}'.format(self.sub_category_name, self.sub_category_description)

    def __as_dict__(self):
        return {
            'sub_category_id': self.sub_category_id,
            'sub_category_name': self.sub_category_name,
            'sub_category_description': self.sub_category_description,
        }

    class Meta:
        db_table = 'sub_category_table'


class ProductVO(models.Model):
    product_id = models.AutoField(db_column="product_id", primary_key=True, null=False)
    product_name = models.CharField(db_column="product_name", max_length=255, default="", null=False)
    product_description = models.TextField(db_column="product_description", max_length=255, default="", null=False)
    product_price = models.IntegerField(db_column="product_price", null=False)
    product_quantity = models.IntegerField(db_column="product_quantity", null=False)
    product_image = models.ImageField(db_column="product_image", upload_to='static/productImages')
    product_category_vo = models.ForeignKey(CategoryVO, on_delete=models.CASCADE, db_column='product_category_id')
    product_sub_category_vo = models.ForeignKey(SubCategoryVO, on_delete=models.CASCADE,
                                                db_column='product_sub_category_id')

    def __str__(self):
        return '{} {} {} {}'.format(self.product_name, self.product_description, self.product_price,
                                    self.product_quantity)

    def __as_dict__(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'product_quantity': self.product_quantity,
            "product_image": self.product_image,
        }

    class Meta:
        db_table = 'product_table'


class LoginVO(models.Model):
    login_id = models.AutoField(db_column="login_id", primary_key=True, null=False)
    login_name = models.CharField(db_column="login_name", max_length=255, default="", null=False)
    login_password = models.CharField(db_column="login_password", max_length=255, null=False)
    login_role = models.CharField(db_column="login_role", max_length=255, null=False)
    login_status = models.CharField(db_column="login_status", max_length=255, null=False)
    login_secret_key = models.CharField(db_column="login_secret_key", max_length=255, null=False)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.login_name, self.login_password, self.login_role, self.login_status, self.login_secret_key)

    def __as_dict__(self):
        return {
            'login_id': self.login_id,
            'login_name': self.login_name,
            'login_password': self.login_password,
            'login_role': self.login_role,
            'login_status': self.login_status,
            'login_secret_key': self.login_secret_key,
        }

    class Meta:
        db_table = 'login_table'


class UserVO(models.Model):
    user_id = models.AutoField(db_column="user_id", primary_key=True, null=False)
    user_first_name = models.CharField(db_column="user_first_name", max_length=255, default="", null=False)
    user_last_name = models.CharField(db_column="user_last_name", max_length=255, null=False)
    user_login_vo = models.ForeignKey(LoginVO, on_delete=models.CASCADE, db_column="user_login_vo")

    def __str__(self):
        return '{} {}'.format(self.user_first_name, self.user_last_name)

    def __as_dict__(self):
        return {
            'user_id': self.user_id,
            'user_first_name': self.user_first_name,
            'user_login_vo': self.user_last_name,
        }

    class Meta:
        db_table = 'user_table'
