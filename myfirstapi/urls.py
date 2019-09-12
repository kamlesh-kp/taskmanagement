"""myfirstapi URL Configuration

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
from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('core/', include('core.urls')),
    path('taskmanagement/', include('taskmanagement.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('employees/', EmployeeList.as_view(), name='employeeList'),
    # path('employee/<int:pk>/', EmployeeDetail.as_view(),name= 'emlpoyeeDetail'),
]
