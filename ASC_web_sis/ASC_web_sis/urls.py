"""
URL configuration for ASC_web_sis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from users import views as views_users
from django.contrib.auth import views as auth_views
 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', views_users.novo_usuario, name='novo_usuario'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('inicial/', views_users.pagina_inicial),
    path('inicial/novaos/', views_users.novaos, name="nova_OS"),
    path('inicial/osdetalhes', views_users.osdetalhes, name="detalhes_das_os" )



    
]
