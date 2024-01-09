from django.db import connection
from django.shortcuts import render
from django.middleware import csrf

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'delete/index.html')


def delete_view(request):
    from deleteApp.models import DeleteUserForm

    if request.method == 'POST':
        form = DeleteUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            # Comprobar que ha inicado sesion el usuario
            user_id = request.session.get('user_id', None)
            if user_id is not None:

                with connection.cursor() as cursor:
                    # Comprobar que es administrador el usuario
                    cursor.execute("SELECT admin FROM registerApp_usuario WHERE username = %s", [user_id])
                    is_admin = cursor.fetchone()[0]

                    if is_admin:
                        # Verificar si el usuario existe antes de intentar eliminarlo
                        cursor.execute("SELECT 1 FROM registerApp_usuario WHERE username = %s", [username])

                        if cursor.fetchone():
                            cursor.execute("DELETE FROM registerApp_usuario WHERE username = %s", [username])
                            return render(request, 'delete/success.html')
                        else:
                            return render(request, 'delete/error.html')
                    else:
                        return render(request, 'delete/needLogin.html')
            else:
                return render(request, 'delete/needLogin.html')
    else:
        return render(request, 'delete/delete.html', {'csrf_token': csrf.get_token(request)})
