from django.urls import path
from . import views
from.views import *



urlpatterns = [
    path('login/',CustomLoginView.as_view(),name="Login"),
    path('',views.index,name="List"),
    path('update/<str:pk>/',views.updateTask,name="Update"),
    path('delete/<str:pk>/',views.deleteTask,name="Delete"),
]