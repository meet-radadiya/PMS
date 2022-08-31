import random
import string

import bcrypt
from django.forms import model_to_dict
from django.shortcuts import render, redirect

from base.models import UserVO, LoginVO

global_login_vo_list = []
global_login_secret_key_set = {0}


def load_login_page(request):
    try:

        return render(request, 'admin/loginPage.html')

    except Exception as exc:

        return render(request, 'admin/error.html', {'message': exc})


def load_register_page(request):
    try:

        return render(request, 'admin/registerPage.html')

    except Exception as exc:

        return render(request, 'admin/error.html', {'message': exc})


def load_admin_index(request):
    try:
        return render(request, 'admin/index.html')

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def load_user_index(request):
    try:
        return render(request, 'user/index.html')

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def insert_user(request):
    try:

        global login_secret_key, secret_key
        global login_secret_key_flag
        login_secret_key_flag = False

        first_name = request.POST.get('regFirstname')
        last_name = request.POST.get('regLastname')
        user_name = request.POST.get('regUsername')
        password = request.POST.get('regPassword')
        role = request.POST.get('regRole')
        status = request.POST.get('regStatus')

        user_vo = UserVO()

        login_vo = LoginVO()

        login_vo_list = LoginVO.objects.all()

        login_secret_key_list = [model_to_dict(i)['login_secret_key'] for i in login_vo_list]

        login_username_list = [model_to_dict(i)['login_user_name'] for i in login_vo_list]

        if user_name in login_username_list:
            error_message = "The username is already exists !"
            return render(request, 'admin/error.html', {'message': error_message})

        while not login_secret_key_flag:
            secret_key = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))

            if secret_key not in login_secret_key_list:
                login_secret_key_flag = True
                break

        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        login_vo.login_name = user_name
        login_vo.login_password = hashed_password.decode('utf-8')
        login_vo.login_role = role
        login_vo.login_status = status
        login_vo.login_secret_key = secret_key

        login_vo.save()

        user_vo.user_first_name = first_name
        user_vo.user_last_name = last_name
        user_vo.user_login_vo = login_vo

        user_vo.save()

        return redirect('/')

    except Exception as exc:

        return render(request, 'admin/error.html', {'message': exc})


def check_user(request):
    try:

        global global_login_vo_list
        global global_login_secret_key_set

        user_name = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword').encode('utf-8')

        login_vo_list = LoginVO.objects.filter(login_name=user_name)

        login_vo_dict = login_vo_list[0].__as_dict__()

        len_login_list = len(login_vo_dict)

        if len_login_list == 0:
            error_message = 'User name is incorrect.'
            return render(request, 'admin/error.html', {'message': error_message})

        elif not login_vo_dict['login_status']:
            error_message = 'You are temporarily blocked.'
            return render(request, 'admin/error.html', {'message': error_message})

        else:
            login_name = login_vo_dict['login_name']
            login_role = login_vo_dict['login_role']
            login_secret_key = login_vo_dict['login_secret_key']
            hashed_login_password = login_vo_dict['login_password'].encode('utf-8')

            if bcrypt.checkpw(password, hashed_login_password):
                login_vo_dict = {login_secret_key: {'login_user_name': login_name, 'login_role': login_role}}

                if len(global_login_vo_list) != 0:

                    for i in global_login_vo_list:

                        temp_list = list(i.keys())
                        global_login_secret_key_set.add(temp_list[0])
                        login_secret_key_list = list(global_login_secret_key_set)

                        if login_secret_key not in login_secret_key_list:
                            global_login_vo_list.append(login_vo_dict)

                else:
                    global_login_vo_list.append(login_vo_dict)

                if login_role == 'admin':
                    response = redirect(load_admin_index)
                    response.set_cookie('login_secret_key',
                                        value=login_secret_key, max_age=1800)
                    response.set_cookie('login_username', value=user_name,
                                        max_age=1800)
                    return response

                elif login_role == 'user':
                    response = redirect(load_user_index)
                    response.set_cookie('login_secret_key',
                                        value=login_secret_key, max_age=1800)
                    response.set_cookie('login_username', value=user_name,
                                        max_age=1800)
                    return response
                else:
                    return redirect(admin_logout_session)
            else:
                error = 'password is incorrect !'
                return render(request, 'admin/error.html', {'message': error})

    except Exception as exc:

        return render(request, 'admin/error.html', {'message': exc})


def admin_login_session(request):
    try:
        global global_login_vo_list
        login_role_flag = ""
        login_secret_key = request.COOKIES.get('login_secret_key')

        if login_secret_key is None:

            return redirect('/')

        for i in global_login_vo_list:

            if login_secret_key in i.keys():

                if i[login_secret_key]['login_role'] == 'admin':

                    login_role_flag = "admin"

                elif i[login_secret_key]['login_role'] == 'user':

                    login_role_flag = "user"

        return login_role_flag

    except Exception as exc:

        return render(request, 'admin/error.html', context={'message': exc})


def admin_logout_session(request):

    try:

        global global_login_vo_list
        login_secret_key = request.COOKIES.get('login_secret_key')
        login_username = request.COOKIES.get('login_username')
        response = redirect('/')

        if login_secret_key is not None and login_username is not None:

            response.set_cookie('login_secret_key', login_secret_key, max_age=0)
            response.set_cookie('login_username', login_username, max_age=0)

            for i in global_login_vo_list:

                if login_secret_key in i.keys():
                    global_login_vo_list.remove(i)
                    break

        return response

    except Exception as exc:

        return render(request, 'admin/error.html', context={'message': exc})
