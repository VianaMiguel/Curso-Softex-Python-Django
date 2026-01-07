# Criar ambiente virtual
python -m venv venv
# Ativar (Linux/Mac)
source venv/bin/activate
# Ativar (Windows)
venv\Scripts\activate
#Passo 2: Instalar Dependências
pip install django djangorestframework django-environ
pip install djangorestframework-simplejwt


python manage.py makemigrations core

python manage.py migrate



Tem que criar o .env e depois criar o secret key

SECRET_KEY=
DEBUG=True


#CRIAR A SECRET KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


python manage.py runserver

#Passo 3: Criar Projeto e App
# Criar projeto Django
django-admin startproject config .
# Criar app core
python manage.py startapp core











""""""
Como usar isso NA PRÁTICA (passo a passo)
1️⃣ Instale o coverage (se não tiver)
pip install coverage

2️⃣ Rode seus testes com coverage
coverage run manage.py test


📌 Isso não mostra nada ainda, só coleta dados.

3️⃣ Gere o relatório HTML
coverage html

4️⃣ Abra no navegador

No Explorer:

htmlcov/index.html


Clique duas vezes ou:

botão direito → abrir com navegador
""""""