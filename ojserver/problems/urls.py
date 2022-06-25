from django.urls import path, include
from . import views

urlpatterns = [
    path('addNewProblem', views.addNewProblem, name='Add New Problem API'),
    path('executeCode', views.executeCode, name='executeCode API')
]
