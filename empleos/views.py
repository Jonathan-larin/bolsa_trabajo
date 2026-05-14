from django.shortcuts import render, redirect  # Agregamos redirect
from django.contrib.auth.models import User    # Agregamos el modelo User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .models import Vacante
from .models import Empresa
from .models import Perfil

def inicio(request):
    return render(request, 'empleos/inicio.html')


def lista_empleos(request):

    vacantes = Vacante.objects.all()

    return render(
        request,
        'empleos/lista_empleos.html',
        {
            'vacantes': vacantes
        }
    )


def detalle_empleo(request):
    return render(request, 'empleos/detalle_empleo.html')


def empresas(request):
    # Traemos todos los registros de la tabla Empresa de tu MySQL80
    lista_de_empresas = Empresa.objects.all()
    
    return render(
        request, 
        'empleos/empresas.html', 
        {
            'empresas': lista_de_empresas  # Enviamos los datos al HTML
        }
    )



def login_view(request):
    if request.method == 'POST':
        # 1. Obtenemos los datos. En Django, por defecto se autentica con 'username'.
        # Si en tu HTML el input dice name="email", cámbialo aquí o en el HTML.
        usuario_o_correo = request.POST.get('email') 
        clave = request.POST.get('password')
        
        # 2. Autenticación
        user = authenticate(request, username=usuario_o_correo, password=clave)
        
        if user is not None:
            login(request, user)
            
            # 3. Redirección basada en el Perfil 
            # Usamos un bloque try/except por si el usuario no tiene perfil aún
            try:
                if user.perfil.tipo_usuario == 'empresa':
                    return redirect('dashboard') # Nombre corregido según tus urlpatterns
                else:
                    return redirect('inicio')
            except AttributeError:
                # Si el usuario existe en auth_user pero no tiene perfil
                return redirect('inicio')
        else:
            # 4. Manejo de error de credenciales
            return render(request, 'empleos/login.html', {
                'error': 'Usuario o contraseña incorrectos',
                'datos': request.POST # Para no borrar lo que el usuario escribió
            })
            
    return render(request, 'empleos/login.html')
def registro(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre')
        usuario = request.POST.get('usuario')
        correo = request.POST.get('email')
        clave = request.POST.get('password')
        tipo = request.POST.get('tipo_usuario')
        
        # 1. Crear el usuario base
        user = User.objects.create_user(
            username=usuario, 
            email=correo, 
            password=clave,
            first_name=nombre_completo
        )
        
        # 2. Crear el Perfil (Esto vincula el tipo de usuario)
        # Nota: Si usas el Trigger que definimos, este paso se puede simplificar
        Perfil.objects.create(usuario=user, tipo_usuario=tipo)
        
        return redirect('login')
        
    return render(request, 'empleos/registro.html')

def dashboard(request):
    return render(request, 'empleos/dashboard.html')


def publicar_empleo(request):
    return render(request, 'empleos/publicar_empleo.html')