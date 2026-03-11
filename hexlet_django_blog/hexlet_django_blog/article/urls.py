from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.home_redirect, name='home'),
    path("articles/<str:tags>/<int:article_id>/",  views.IndexView.as_view(), name='article'),
    path("<int:id>/", views.ArticleView.as_view(), name='article_detail'),
    path('<int:article_id>/comments/<int:id>/', views.ArticleCommentsView.as_view(), name='comment_detail')
]