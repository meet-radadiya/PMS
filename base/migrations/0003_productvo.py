# Generated by Django 3.0.1 on 2022-05-10 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0002_subcategoryvo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVO',
            fields=[
                ('product_id', models.AutoField(db_column='product_id', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='product_name', default='', max_length=255)),
                ('product_description', models.TextField(db_column='product_description', default='', max_length=255)),
                ('product_price', models.IntegerField(db_column='product_price')),
                ('product_quantity', models.IntegerField(db_column='product_quantity')),
                ('product_image', models.ImageField(db_column='product_image', upload_to='static/productImages')),
                ('product_category_vo',
                 models.ForeignKey(db_column='product_category_id', on_delete=django.db.models.deletion.CASCADE,
                                   to='base.CategoryVO')),
                ('product_sub_category_vo',
                 models.ForeignKey(db_column='product_sub_category_id', on_delete=django.db.models.deletion.CASCADE,
                                   to='base.SubCategoryVO')),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
    ]
