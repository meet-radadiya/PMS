from django.shortcuts import render, redirect

from base.login_view import admin_login_session, admin_logout_session
from base.models import CategoryVO


def load_category_insert(request):
    try:
        if admin_login_session(request) == 'admin':
            return render(request, 'admin/insertCategory.html')
        else:
            return admin_logout_session(request)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def insert_category(request):
    try:
        if admin_login_session(request) == 'admin':
            category_name = request.POST.get('categoryName')
            category_description = request.POST.get('categoryDescription')

            category_vo = CategoryVO()

            category_vo.category_name = category_name
            category_vo.category_description = category_description

            category_vo.save()

            return redirect(view_category)
        else:
            return admin_logout_session(request)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_category(request):
    try:
        if admin_login_session(request) == 'admin':
            category_vo_list = CategoryVO.objects.all()

            return render(request, 'admin/viewCategory.html', {'category_vo_list': category_vo_list})
        else:
            return admin_logout_session(request)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_category_user(request):
    try:
        if admin_login_session(request) == 'user':
            category_vo_list = CategoryVO.objects.all()

            return render(request, 'user/viewCategory.html', {'category_vo_list': category_vo_list})
        else:
            return admin_logout_session(request)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def delete_category(request):
    try:
        if admin_login_session(request) == 'admin':
            category_id = request.GET.get('categoryId')

            category_vo = CategoryVO()

            category_vo.category_id = category_id

            category_vo.delete()

            return redirect(view_category)
        else:
            return admin_logout_session(request)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def edit_category(request):
    try:
        if admin_login_session(request) == 'admin':
            category_id = request.GET.get('categoryId')

            category_vo = CategoryVO()

            category_vo.category_id = category_id

            category_vo_list = CategoryVO.objects.get(category_id=category_id)
            # category_vo_list_obj = CategoryVO.objects.filter(category_id=category_id)
            # # category_vo_list = category_vo_list_obj[0]

            return render(request, 'admin/editCategory.html', {'category_vo_list': category_vo_list})
        else:
            return admin_logout_session(request)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def update_category(request):
    try:
        if admin_login_session(request) == 'admin':
            category_id = request.POST.get('categoryId')
            category_name = request.POST.get('categoryName')
            category_description = request.POST.get('categoryDescription')

            category_vo = CategoryVO()

            category_vo.category_id = category_id
            category_vo.category_name = category_name
            category_vo.category_description = category_description

            category_vo.save()

            return redirect(view_category)
        else:
            return admin_logout_session(request)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})

