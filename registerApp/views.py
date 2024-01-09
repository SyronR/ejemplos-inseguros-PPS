from django.contrib.auth.hashers import make_password
from django.db import connection
from django.middleware import csrf
from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'register/index.html')


def register_view(request):
    from registerApp.models import Usuario, RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            admin = request.POST.get('admin', "off")

            # Cifrar la contraseña del usuario
            hashed_passwd = make_password(password)

            # Utilizando sentencia SQL Segura para obtener el usuario por nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registerApp_usuario WHERE username = %s;", [username])
                user_exits = cursor.fetchone()

            if user_exits:
                return render(request, 'register/error.html')
            else:
                # Crear un objeto usuario donde se guardan los valores internamente
                user = Usuario()
                user.username = username
                user.password = hashed_passwd
                if admin == "on":
                    user.admin = True
                else:
                    user.admin = False
                user.save()

                return render(request, 'register/success.html')
    else:
        return render(request, 'register/register.html', {'csrf_token': csrf.get_token(request)})
