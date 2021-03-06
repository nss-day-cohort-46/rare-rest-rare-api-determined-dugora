"""
rare URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rareapi.views.tag import TagView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rareapi.views import PostViewSet
from django.contrib import admin
from rareapi.views import login_user, register_user
from rareapi.models.category import Category
from rareapi.views.category import CategoryView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', TagView, 'tag')
router.register(r'posts', PostViewSet, 'post')
router.register(r'categories', CategoryView, 'category')


urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
]
