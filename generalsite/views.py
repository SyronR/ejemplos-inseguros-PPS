from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'index/index.html')