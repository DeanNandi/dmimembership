from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('patients-form', views.my_form, name='patients-form'),
    path('login', views.loginPage, name="login"),
    path('register', views.registerPage, name="register"),
    path('logout', views.logoutUser, name="logout"),
    path('delete-patient/(?P<pk>\d+)', views.delete_patient, name='delete-patient/(?P<pk>\d+)'),
]
