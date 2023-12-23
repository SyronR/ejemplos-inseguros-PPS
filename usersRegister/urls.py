from django.urls import path

from usersRegister.views import *

urlpatterns = [
    path('register/', register_view),
    path('', index_view)
]