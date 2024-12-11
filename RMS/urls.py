"""
URL configuration for RMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from restaurant.views import TableViewSet, CategoryViewSet, MenuViewSet, OrderViewSet, WaiterViewSet, ReceptionViewSet


router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'menu-items', MenuViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'waiters', WaiterViewSet)
router.register(r'receptions', ReceptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
