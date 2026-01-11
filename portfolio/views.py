from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Proyecto

def home(request):
    # --- LÓGICA DE FORMULARIO DE CONTACTO ---
    if request.method == "POST":
        # 1. Obtenemos los datos del HTML (coinciden con el atributo name="")
        nombre = request.POST.get('name')
        email_cliente = request.POST.get('email')
        mensaje = request.POST.get('message')

        # 2. Validamos que no lleguen vacíos
        if nombre and email_cliente and mensaje:
            try:
                # 3. Preparamos el asunto y el cuerpo del correo
                asunto = f"Nuevo Mensaje de Portfolio: {nombre}"
                cuerpo_correo = f"""
                Has recibido un nuevo contacto desde tu web.
                
                -----------------------------------
                Nombre: {nombre}
                Email: {email_cliente}
                
                Mensaje:
                {mensaje}
                -----------------------------------
                """
                
                # 4. Enviamos el mail
                send_mail(
                    asunto,
                    cuerpo_correo,
                    settings.EMAIL_HOST_USER,  # Remitente (tu propio gmail configurado en settings)
                    ['dariojr666@gmail.com'],    # <--- ¡CAMBIA ESTO POR TU EMAIL REAL!
                    fail_silently=False,
                )

                # 5. Feedback positivo
                messages.success(request, "¡Tu mensaje ha sido enviado correctamente!")
                
                # Redirigimos a la misma vista para limpiar el formulario (evita reenvíos al actualizar)
                return redirect('home')

            except Exception as e:
                # Si falla (ej: sin internet o clave mal puesta), avisamos sin romper la página
                messages.error(request, "Hubo un error al enviar el mensaje. Intenta nuevamente.")
                print(f"Error enviando mail: {e}")
        else:
            messages.warning(request, "Por favor completa todos los campos del formulario.")

    # --- LÓGICA DE CARGA DE PÁGINA (GET) ---
    
    # Traemos todos los proyectos de la base de datos (tu código original)
    proyectos = Proyecto.objects.all()
    
    # Renderizamos el HTML enviándole los datos y los mensajes
    return render(request, 'portfolio/index.html', {'proyectos': proyectos})