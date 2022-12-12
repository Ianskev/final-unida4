from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="session-home"),
    path('crear/',views.CreateProject.as_view(), name="crear"),
]