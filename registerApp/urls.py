from django.urls import path
from registerApp.views import *

urlpatterns = [
    path('', index_view),
    path('register/', register_view)
]