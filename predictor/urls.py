from django.urls import path
from .views import chatbot, predict

urlpatterns = [
    path('chatbot/', chatbot),
    path('predict/', predict),
]