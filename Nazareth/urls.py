from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('sign/',views.signup,name="sign"),
    path('patients/',views.patients,name="patients"),
    path('doctors/',views.doctors,name="doctors"),
    path('technicians/',views.technicians,name="technicians"),
    path('appointment/',views.appointment,name="appointment"),
    path('nurses/',views.nurses,name="nurses"),
    path('search_results/',views.search_results,name="search"),
    
  
]

