from django.shortcuts import render

# Aqui se definen los metodos que renderizaran los templates que contienen los HTMLs


def index_view(request):
    return render(request, 'register/index.html')


def register_view(request):
    from usersRegister.models import Usuario

    if request.GET:
        username = request.GET['username']
        passwd = request.GET['password']

        print(f'username: {username}')
        print(f'password: {passwd}')

        # Crear un objeto usuario donde se guardan los valores internamente

        user = Usuario()
        user.username = username
        user.password = passwd
        user.save()

        return render(request, 'register/success.html')
    else:
        return render(request, 'register/register.html')
