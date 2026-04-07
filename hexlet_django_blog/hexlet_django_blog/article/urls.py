from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.home_redirect, name='home'),
    path("articles/<str:tags>/<int:article_id>/",  views.IndexView.as_view(), name='article'),
    path("<int:id>/edit/", views.ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/", views.ArticleView.as_view(), name='article_detail'),
    path('<int:article_id>/comments/<int:id>/', views.ArticleCommentsView.as_view(), name='comment_detail'),
    path('articles/<int:article_id>/comments/add/', views.ArticleCommentFormView.as_view(), name='add_comment'),
    path("create/", views.ArticleFormCreateView.as_view(), name="articles_create"),
]
