from django.contrib import admin
from .models import Tarefa # 1. Importe seu Model

# Register your models here.

# 2. "Registre" seu Model no site de administração
admin.site.register(Tarefa)

#Usuário : admin
#Endereço : admin@admin.com
#Senha: admin
