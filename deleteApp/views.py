from django.db import connection
from django.shortcuts import render
from deleteApp.models import DeleteUserForm

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'delete/index.html')


def delete_view(request):

    if request.GET:
        form = DeleteUserForm(request.GET)

        if form.is_valid():
            username = form.cleaned_data['username']

            # Verificar si el usuario existe antes de intentar eliminarlo
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM registerApp_usuario WHERE username = %s", [username])
                user_exists = cursor.fetchone()

            # Si el usuario existe, se elimina, sin, se informa al usuario
            if user_exists:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM registerApp_usuario WHERE username = %s", [username])

                return render(request, 'delete/success.html')
            else:
                return render(request, 'delete/error.html')

    else:
        return render(request, 'delete/delete.html')
