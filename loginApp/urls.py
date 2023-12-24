from django.urls import path
from loginApp.views import *

urlpatterns = [
    path('', index_view),
    path('login/', login_view)
]