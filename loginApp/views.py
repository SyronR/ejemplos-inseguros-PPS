from django.contrib.auth.hashers import check_password
from django.db import connection
from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'login/index.html')


def login_view(request):
    from loginApp.models import LoginForm

    if request.GET:
        form = LoginForm(request.GET)

        if form.is_valid():
            # Obtener el nombre de usuario y la contraseña del login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Utilizando sentencia RAW SQL para obtener el usuario por nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registerApp_usuario WHERE username = %s", [username])
                user_row = cursor.fetchone()

                # print(user_row)

            # Verifica la contraseña, en caso de estar cifrada la contraseña, hay que usar chech_password:
            # if user_row and check_password(password, user_row[1]):
            if user_row and user_row[1] == password:
                # Almacena el ID del usuario en la sesión
                request.session['user_id'] = user_row[0]

                return render(request, 'login/success.html')
            else:
                return render(request, 'login/error.html')

    else:
        return render(request, 'login/login.html')
