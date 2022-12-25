"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    # Web Services
    path('ws/movies/<str:sort>', views.movie_list),
    path('ws/movie/<int:movie_id>', views.movie_detail),
    path('ws/movie', views.create_movie),
    path('ws/movie/<int:movie_id>', views.update_movie),
    path('ws/movie/<int:movie_id>', views.delete_movie),
]