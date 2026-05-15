from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('empleos/', views.lista_empleos, name='lista_empleos'),
    path('detalle/', views.detalle_empleo, name='detalle_empleo'),
    path('empresas/', views.empresas, name='empresas'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('publicar/', views.publicar_empleo, name='publicar_empleo'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]