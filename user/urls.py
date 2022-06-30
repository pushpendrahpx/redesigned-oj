from django.urls import include, path
from . import views
urlpatterns = [
        path('register/', views.register, name='Register users API'),
        path('login/', views.login, name='Login users API'),
        path('getProfile/', views.getProfile, name='Login users API')
]
