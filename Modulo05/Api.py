# Criar ambiente virtual
python -m venv venv
# Ativar (Linux/Mac)
source venv/bin/activate
# Ativar (Windows)
venv\Scripts\activate
#Passo 2: Instalar Dependências
pip install django djangorestframework django-environ
djangorestframework-simplejwt

#Passo 3: Criar Projeto e App
# Criar projeto Django
django-admin startproject config .
# Criar app core
python manage.py startapp core

#CRIAR A SECRET KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"