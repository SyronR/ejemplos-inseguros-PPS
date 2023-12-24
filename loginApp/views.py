from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'login/index.html')


def login_view(request):

    if request.GET:
        return render(request, 'login/success.html')
    else:
        return render(request, 'login/login.html')
