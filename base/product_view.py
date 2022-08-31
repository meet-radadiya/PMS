import json
import os
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from base.models import CategoryVO, SubCategoryVO, ProductVO


def load_product_insert(request):
    try:

        category_vo_list = CategoryVO.objects.all()

        return render(request, 'admin/addProduct.html', {'category_vo_list': category_vo_list})
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def load_product_sub_category(request):
    try:

        category_id = request.GET.get('category_id')

        category_vo = CategoryVO()

        category_vo.category_id = category_id

        sub_category_vo = SubCategoryVO.objects.filter(sub_category_category_vo=category_vo)

        sub_category_list = [model_to_dict(i) for i in sub_category_vo]

        return HttpResponse(json.dumps(sub_category_list), content_type='application/json')

    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def insert_product(request):
    try:

        product_name = request.POST.get('productName')
        product_description = request.POST.get('productDescription')
        product_price = request.POST.get('productPrice')
        product_quantity = request.POST.get('productQuantity')
        product_file = request.FILES.get('productFile')
        product_category = request.POST.get('productCategoryDropdown')
        product_sub_category = request.POST.get('productSubCategoryDropdown')

        category_vo = CategoryVO()

        category_vo.category_id = product_category

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_id = product_sub_category

        product_vo = ProductVO()

        product_vo.product_name = product_name
        product_vo.product_description = product_description
        product_vo.product_price = product_price
        product_vo.product_quantity = product_quantity
        product_vo.product_image = product_file
        product_vo.product_category_vo = category_vo
        product_vo.product_sub_category_vo = sub_category_vo

        product_vo.save()

        return redirect(view_product)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_product(request):
    try:
        product_list = ProductVO.objects.all()
        return render(request, 'admin/viewProduct.html', {'product_list': product_list})
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def view_product_user(request):
    try:
        product_list = ProductVO.objects.all()
        return render(request, 'user/viewProduct.html', {'product_list': product_list})
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def delete_product(request):
    try:

        product_id = request.GET.get('productId')
        file_path = request.GET.get('imagePath')

        product_vo = ProductVO()

        product_vo.product_id = product_id

        product_vo.delete()

        os.remove(file_path)

        return redirect(view_product)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def edit_product(request):
    try:
        product_id = request.GET.get('productId')

        product_vo = ProductVO()

        product_vo.product_id = product_id

        product_vo_list = ProductVO.objects.filter(product_id=product_id)

        category_vo_list = CategoryVO.objects.all()

        return render(request, 'admin/editProduct.html',
                      {'product_vo_list': product_vo_list, 'category_vo_list': category_vo_list})
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})


def update_product(request):
    try:
        product_id = request.POST.get('productId')
        product_name = request.POST.get('productName')
        product_description = request.POST.get('productDescription')
        product_price = request.POST.get('productPrice')
        product_quantity = request.POST.get('productQuantity')
        product_file = request.POST.get('productImage')
        product_category = request.POST.get('productCategoryDropdown')
        product_sub_category = request.POST.get('productSubCategoryDropdown')

        category_vo = CategoryVO()

        category_vo.category_id = product_category

        sub_category_vo = SubCategoryVO()

        sub_category_vo.sub_category_id = product_sub_category

        product_vo = ProductVO()

        product_vo.product_id = product_id
        product_vo.product_name = product_name
        product_vo.product_description = product_description
        product_vo.product_price = product_price
        product_vo.product_quantity = product_quantity
        product_vo.product_image = product_file
        product_vo.product_category_vo = category_vo
        product_vo.product_sub_category_vo = sub_category_vo

        product_vo.save()

        return redirect(view_product)
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})
