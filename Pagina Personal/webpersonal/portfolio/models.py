from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(max_length=200, verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    url = models.URLField(max_length=200, verbose_name="Enlace de sitio web", blank=True, null=True)

    #subclase para añadir metadatos a al modelo
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        #campo para ordenar los proyectos
        ordering = ['-created']

    def __str__(self):
        return self.title