from django.urls import include, path
from . import views
urlpatterns = [
        path('index/', views.index, name='main-view'),
]
