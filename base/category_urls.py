from django.urls import path

from . import category_view

urlpatterns = [
    path('load_insert_category/', category_view.load_category_insert, name='load_insert_category'),
    path('insert_category/', category_view.insert_category, name='insert_category'),
    path('view_category/', category_view.view_category, name='view_category'),
    path('delete_category/', category_view.delete_category, name='delete_category'),
    path('edit_category/', category_view.edit_category, name='edit_category'),
    path('update_category/', category_view.update_category, name='update_category'),
    path('user_view_category/', category_view.view_category_user, name='view_category_user')
]
