from django.shortcuts import render, redirect

from base.models import CategoryVO, SubCategoryVO


def load_sub_category_insert(request):
    try:
        category_vo_list = CategoryVO.objects.all()
        return render(request, 'admin/addSubCategory.html', {'category_vo_list': category_vo_list})

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def insert_sub_category(request):
    try:

        category_id = request.POST.get('subcategoryDropdown')

        sub_category_name = request.POST.get('subcategoryName')

        sub_category_description = request.POST.get('subcategoryDescription')

        category_vo = CategoryVO()

        category_vo.category_id = category_id

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_name = sub_category_name
        sub_category_vo.sub_category_description = sub_category_description
        sub_category_vo.sub_category_category_vo = category_vo

        sub_category_vo.save()

        return redirect(view_sub_category)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_sub_category(request):
    try:
        sub_category_vo_list = SubCategoryVO.objects.all()

        return render(request, 'admin/viewSubCategory.html', {'sub_category_vo_list': sub_category_vo_list})

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_sub_category_user(request):
    try:
        sub_category_vo_list = SubCategoryVO.objects.all()

        return render(request, 'user/viewSubCategory.html', {'sub_category_vo_list': sub_category_vo_list})

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def delete_sub_category(request):
    try:

        sub_category_id = request.GET.get('subcategoryId')

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_id = sub_category_id

        sub_category_vo.delete()

        return redirect(view_sub_category)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def edit_sub_category(request):
    try:

        sub_category_id = request.GET.get('subcategoryId')

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_id = sub_category_id

        sub_category_vo_list = SubCategoryVO.objects.get(sub_category_id=sub_category_id)

        category_vo_list = CategoryVO.objects.all()

        return render(request, 'admin/editSubCategory.html',
                      {'subcategory_vo_list': sub_category_vo_list, 'category_vo_list': category_vo_list})

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def update_sub_category(request):
    try:

        category_id = request.POST.get('categoryId')

        sub_category_name = request.POST.get('subcategoryName')

        sub_category_description = request.POST.get('subcategoryDescription')

        sub_category_id = request.POST.get('subcategoryId')

        category_vo = CategoryVO()

        category_vo.category_id = category_id

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_id = sub_category_id
        sub_category_vo.sub_category_name = sub_category_name
        sub_category_vo.sub_category_description = sub_category_description
        sub_category_vo.sub_category_category_vo = category_vo

        sub_category_vo.save()

        return redirect(view_sub_category)

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})
