from django.shortcuts import render

def inicio(request):
    return render(request, 'empleos/inicio.html')

def lista_empleos(request):
    return render(request, 'empleos/lista_empleos.html')

def detalle_empleo(request):
    return render(request, 'empleos/detalle_empleo.html')

def empresas(request):
    return render(request, 'empleos/empresas.html')

def login_view(request):
    return render(request, 'empleos/login.html')

def registro(request):
    return render(request, 'empleos/registro.html')

def dashboard(request):
    return render(request, 'empleos/dashboard.html')

def publicar_empleo(request):
    return render(request, 'empleos/publicar_empleo.html')