from django.shortcuts import render
from django.http import HttpRequest, HttpResponse #print en la web, podemos imprimir cod de html

# Create your views here.
def saludo(request):
    return HttpResponse(f"Hola Mundo! quieres ir al saludo especial? click <a href='/territorio/saludoEspecial/hola'>aqui</a>")

def saludoEspecial(request, vari):
    if vari == "":
        pass
    else:
        return HttpResponse(f"<strong>Hey</strong>, este es un nuevo saludo, por cierto {vari}<br>quieres ir al saludo comun? click <a href='/territorio/saludar'>aqui</a>")

def calculadora(request, tipo, vari, vari2):
    if tipo == 1:
        HttpResponse("sumita")
        return HttpResponse(f"la suma es: <br><strong>{vari} + {vari2} =</strong> <a style='color:red';>{vari + vari2}</a>")
    elif tipo==2:
        return HttpResponse(f"la resta es: <br><strong>{vari} - {vari2} =</strong> <a style='color:red';>{vari - vari2}</a>")
    elif tipo==3:
        return HttpResponse(f"la multiplicacion es: <br><strong>{vari} * {vari2} =</strong> <a style='color:red';>{vari * vari2}</a>")
    elif tipo==4:
        return HttpResponse(f"la division es: <br><strong>{vari} / {vari2} =</strong> <a style='color:red';>{vari/vari2}</a>")

def inicio(request):
    return render(request, 'territorio/index.html')

def loginForm(request):
    return render(request, 'territorio/login/login.html')

def login(request):
    u = request.POST["usuario"]
    c = request.POST["clave"]
    if u == "admin" and c=="1234":
        return HttpResponse(f"Bienvenido {u}")
    else:
        return HttpResponse("acceso denegado")



    

