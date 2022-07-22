from django.urls import path

from . import views

app_name="territorio"

urlpatterns = [
    path('saludar/', views.saludo, name="saludar"),
    path('saludoEspecial/<str:vari>', views.saludoEspecial, name="saludar"), #vari tiene que ir en el metodo 
    path('calculadora/<int:tipo>/<int:vari>/<int:vari2>', views.calculadora, name="calculadora"), #vari tiene que ir en el metodo 
    path('', views.inicio, name="inicio"),
    path('loginForm/', views.loginForm, name="login-form"),
    path('login/', views.login, name="login"),
]

