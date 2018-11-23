from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"

urlpatterns = [

    path('',views.home, name="home"),
    path('secret/',views.secret_page,name="secret"),
    path('secret2/',views.SecretPage.as_view(),name="secret2"),
    path('add/',views.add_new,name="add"),
]