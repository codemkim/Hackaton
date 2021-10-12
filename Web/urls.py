from django.contrib import admin
from django.urls import path, include
from Web import views

app_name ='time_travel'

urlpatterns = [
    path('', views.predict, name='predict_page'),
    path('make_ani/', views.make_ani, name ="make_ani"),
]