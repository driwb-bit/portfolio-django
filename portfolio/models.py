from django.db import models
from django.db import models
from PIL import Image, ImageOps  # <--- Importaciones nuevas necesarias
import os

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    tema = models.CharField(max_length=100, verbose_name="Tema (ej: App Ventas, IA)")
    descripcion = models.TextField(verbose_name="Descripción Breve")
    imagen = models.ImageField(upload_to="proyectos/", verbose_name="Imagen del Proyecto")
    enlace = models.URLField(null=True, blank=True, verbose_name="Enlace al Proyecto (Deploy)")
    fecha = models.DateField(verbose_name="Fecha de Realización")
    tecnologias = models.CharField(max_length=200, verbose_name="Tecnologías")
    repositorio = models.URLField(null=True, blank=True, verbose_name="Enlace al Repo (GitHub)")
    publicado = models.BooleanField(default=True, verbose_name="¿Visible?")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha']

    def __str__(self):
        return self.nombre

    # --- AQUÍ ESTÁ LA MAGIA ---
    def save(self, *args, **kwargs):
        # 1. Primero guardamos la imagen original en el disco
        super().save(*args, **kwargs)

        # 2. Abrimos la imagen que acabamos de guardar
        if self.imagen:
            img = Image.open(self.imagen.path)

            # 3. Definimos las dimensiones deseadas (Ancho x Alto)
            # Ejemplo: 800x600 (Formato rectangular estándar)
            output_size = (800, 600)

            # 4. Verificamos si es necesario recortar
            if img.height != 600 or img.width != 800:
                # ImageOps.fit recorta el centro (Smart Crop) y redimensiona
                img = ImageOps.fit(img, output_size, method=Image.Resampling.LANCZOS)
                
                # 5. Sobrescribimos el archivo original con la versión recortada
                img.save(self.imagen.path)