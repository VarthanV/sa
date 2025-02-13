"""student_analytica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from console import views as console_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('console.urls')),
    path('login/',console_views.Login.as_view(),name='login'),
    path('logout/',console_views.LogoutView.as_view(),name='logout'),
    path('jobs/add_student/', user_views.add_student, name='add_student'),
    path('jobs/add_staff/', user_views.add_staff, name='add_staff'),


]
