"""
URL configuration for mangiamo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.display_about_page, name="about"),
    path("recipes/<int:recipe_id>", views.display_recipe, name="recipe"),
    path("authors/<int:author_id>", views.display_author, name="author"),
    path("artisans", views.display_authors_page, name="authors"),
    path("search", views.search_page, name="search"),
    path("create", views.create_page, name="create_recipe"),
    path("create/thanks", views.create_thanks, name="create_thanks")
]

admin.site.site_header = 'Mangiamo! Admin'
admin.site.site_title = 'Mangiamo!'