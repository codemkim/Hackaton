from django.contrib import admin
from django.urls import path, include
from Web import views

app_name ='time_travel'

urlpatterns = [
    path('', views.predict, name='predict_page'),
    path('make_ani_1/', views.make_ani_1, name ="make_ani_1"),
    path('make_ani_2/', views.make_ani_2, name ="make_ani_2"),
]