from django.urls import path

from . import login_view

urlpatterns = [
    path('insert_user/', login_view.insert_user, name='insert_user'),
    path('login_user/', login_view.load_login_page, name='load_login_page'),
    path('register_user/', login_view.load_register_page, name='load_register_user'),
    path('load_admin_index/', login_view.load_admin_index, name='load_admin_index'),
    path('load_user_index/', login_view.load_user_index, name='load_user_index'),
    path('check_user/', login_view.check_user, name='check_user_credentials'),
]
