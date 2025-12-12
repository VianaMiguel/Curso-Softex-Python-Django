"""
✅ CHECKLIST COMPLETO — PARA RODAR O PROJETO DO ZERO
1. Entrar no projeto
cd TCC

2. Criar o ambiente virtual (somente 1 vez)
python -m venv venv

3. Ativar o ambiente virtual
Windows
venv\Scripts\activate

Linux/Mac
source venv/bin/activate


⚠️ IMPORTANTE: TODO comando abaixo só funciona com o ambiente ativado.

4. Instalar todas as dependências do projeto

Instala tudo que você usa:

pip install django
pip install djangorestframework
pip install django-environ
pip install djangorestframework-simplejwt
pip install python-decouple


Ou, se quiser instalar tudo de uma vez:

pip install django djangorestframework django-environ djangorestframework-simplejwt python-decouple

5. Fazer migrações de todos os apps

(para criar as tabelas no banco)

Users:
python manage.py makemigrations users

Core:
python manage.py makemigrations core

Aplicar tudo no banco:
python manage.py migrate

6. Rodar o servidor
python manage.py runserver""""""