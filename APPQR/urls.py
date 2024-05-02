# QRCODEAPP/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL para a página inicial
    path('gerar_qrcode/', views.gerar_qrcode, name='gerar_qrcode'),  # URL para a view que gera o QR code
]
