"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from src.interfaces import views
from src.interfaces import post_views
from src.interfaces.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterUserView.as_view(), name="register"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("post/create/", post_views.create_post, name="post_create"),
    path('posts/', post_views.PostListCreateView.as_view(), name='post-list'),
    path("edit-post/<int:post_id>/", post_views.edit_post, name="edit_post"),
    path('posts/<int:pk>/', post_views.PostDetailView.as_view(), name='post-detail'),
    path("delete-post/<int:post_id>/", post_views.delete_post, name="delete_post"),

    path("admin/", admin.site.urls),
]
