from django.urls import path
from mainpage.views import *

urlpatterns = [
    path('', view_home),
    path('contato', view_contato)
]