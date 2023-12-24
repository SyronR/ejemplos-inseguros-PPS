from django.db import connection
from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'register/index.html')


def register_view(request):
    from registerApp.models import Usuario, RegisterForm

    if request.GET:
        form = RegisterForm(request.GET)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Utilizando sentencia RAW SQL para obtener el usuario por nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registerApp_usuario WHERE username = %s", [username])
                user_exits = cursor.fetchone()

            if user_exits:
                return render(request, 'register/error.html')
            else:
                # Crear un objeto usuario donde se guardan los valores internamente
                user = Usuario()
                user.username = username
                user.password = password
                user.save()

                return render(request, 'register/success.html')
    else:
        return render(request, 'register/register.html')
