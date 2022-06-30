from django.urls import include, path
from . import views
urlpatterns = [
        path('create_problem/', views.create_problem, name='main-view'),
]
