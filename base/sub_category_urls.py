from django.urls import path

from . import sub_category_view

urlpatterns = [
    path('load_insert_sub_category/', sub_category_view.load_sub_category_insert, name='load_insert_sub_category'),
    path('insert_sub_category/', sub_category_view.insert_sub_category, name='insert_sub_category'),
    path('view_sub_category/', sub_category_view.view_sub_category, name='view_sub_category'),
    path('delete_sub_category/', sub_category_view.delete_sub_category, name='delete_sub_category'),
    path('edit_sub_category/', sub_category_view.edit_sub_category, name='edit_sub_category'),
    path('update_sub_category/', sub_category_view.update_sub_category, name='update_sub_category'),
    path('user_view_sub_category/', sub_category_view.view_sub_category_user, name='user_view_sub_category'),

]
