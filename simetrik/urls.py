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
from django.conf import settings
from django.conf.urls.static import static
from users.views import ObtainTokenCustom, UserProfileViewSet
from upload_file.views import UploadFileViewSet


router = DefaultRouter()
# Users Routes
router.register(r'users', UserProfileViewSet, basename='user')
changes_password = UserProfileViewSet.as_view({'put': 'change_password'})
# Upload File Routes
router.register(r'upload_files', UploadFileViewSet, basename='upload_file')

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/user/obtain_token/', ObtainTokenCustom.as_view()),
    path('api/v1/users/change_password/<int:pk>/', changes_password),

    # Includin all routes
    path('api/v1/', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
