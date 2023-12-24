from django.urls import path
from deleteApp.views import *

urlpatterns = [
    path('', index_view),
    path('delete/', delete_view)
]