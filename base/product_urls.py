from django.urls import path

from . import product_view

urlpatterns = [
    path('load_product/', product_view.load_product_insert, name='load_insert_product'),
    path('load_product_sub_category', product_view.load_product_sub_category, name='load_product_sub_category'),
    path('insert_product/', product_view.insert_product, name='insert_product'),
    path('view_product/', product_view.view_product, name='view_product'),
    path('delete_product/', product_view.delete_product, name='delete_product'),
    path('edit_product/', product_view.edit_product, name='edit_product'),
    path('update_product/', product_view.update_product, name='update_product'),
    path('user_view_product/', product_view.view_product_user, name='user_view_product'),
]
