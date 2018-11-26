from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app"

urlpatterns = [

    path('',views.home, name="home"),
    path('secret/',views.secret_page,name="secret"),
    path('add/',views.AddPost.as_view(),name="addpost"),
    path('<int:pk>/update/',views.UpdatePost.as_view(),name="updatepost"),
    path('<int:pk>/delete/',views.DeletePost.as_view(),name="deletepost"),
    # path('secret2/',views.SecretPage.as_view(),name="secret2"),
]