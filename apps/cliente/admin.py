from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
    
        )
    list_filter=(
        'nombre',
        'apellido',
        'active',
        'disponible',
        )
    ordering=(
        'nombre',
        'apellido',
        'dni',
    
    )
    search_fields=(
        'nombre',
        'apellido',
        'dni',
        
    )
    

# Register your models here.
