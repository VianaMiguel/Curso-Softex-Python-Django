"""
URL configuration for meuprojeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# meuprojeto/urls.py
from django.contrib import admin
from django.urls import path, include # 1. Importe o 'include'
from django.contrib.auth import views as auth_views # 1. Importe as views de autenticação

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('core.urls')), # 2. Adicione esta linha, Nossas URLs do app 'core'
path('login/', auth_views.LoginView.as_view(template_name='login.html'), # Ela usa a View pronta 'LoginView' e diz a ela para usar nosso template
 name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='login'), # Ela usa a View 'LogoutView'. 'next_page' diz para onde ir após o logout
 name='logout'),
]
