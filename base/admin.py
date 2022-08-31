from django.contrib import admin
from .models import CategoryVO, SubCategoryVO, ProductVO, LoginVO, UserVO

# Register your models here.
admin.site.register(CategoryVO)
admin.site.register(SubCategoryVO)
admin.site.register(ProductVO)
admin.site.register(LoginVO)
admin.site.register(UserVO)
