from django.contrib import admin
# importamos el modelo 
from .models import Project


# Register your models here.
class CreacionModificacion(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    fields = ('title', 'description', 'image', 'url')

#activamos el modelo en el panel de Super Administrador
admin.site.register(Project, CreacionModificacion)   