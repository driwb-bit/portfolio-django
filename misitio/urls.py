from django.contrib import admin
from django.urls import path
from portfolio import views # Importamos la vista que acabamos de crear
from django.conf import settings # Importante para las imágenes
from django.conf.urls.static import static # Importante para las imágenes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # La ruta vacía '' significa la página de inicio
]

# Esto es MAGIA necesaria para que se vean las imágenes que subas en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
