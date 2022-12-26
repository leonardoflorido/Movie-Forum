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
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app import views

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Forum API",
        default_version='v1',
        description="REST API for Movie Forum",
    ),
    public=True,
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    # Directors Web Services
    path('ws/directors/', views.director_list),
    path('ws/director/<int:director_id>/', views.director_detail),
    # Movies Web Services
    path('ws/movies/<str:sort_by>', views.movie_list),
    path('ws/movie/<int:movie_id>', views.movie_detail),
    path('ws/movie', views.create_movie),
    path('ws/movie/<int:movie_id>', views.update_movie),
    path('ws/movie/<int:movie_id>', views.delete_movie),
]
