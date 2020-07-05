"""simetrik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.urls import include
from users.views import ObtainTokenCustom, UserProfileViewSet


router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user')

changes_password = UserProfileViewSet.as_view({'put': 'change_password'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/obtain_token/', ObtainTokenCustom.as_view()),
    path('api/v1/users/change_password/<int:pk>', changes_password),

    path('api/v1/', include(router.urls)),

]
