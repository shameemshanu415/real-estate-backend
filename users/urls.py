from django.urls import path
from .views import register, login   # ❌ remove profile

urlpatterns = [
    path('register/', register),
    path('login/', login),
]