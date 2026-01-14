from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.home_redirect, name='home'),
    path("articles/<str:tags>/<int:article_id>/", views.index, name='article'),
]