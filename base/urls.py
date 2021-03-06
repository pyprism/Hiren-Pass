from django.urls import path, include
from base import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('settings', views.SettingsModelView)

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', include(router.urls)),
]

