from django.shortcuts import render


# Create your views here.
def login(request):
    try:
        return render(request, 'admin/loginPage.html')
    except Exception as exc:
        return render(request, 'admin/error.html', {'message': exc})
