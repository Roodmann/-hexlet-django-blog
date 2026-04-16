from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from hexlet_django_blog.article.models import Article
from .forms import RegistrationForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        context["articles"] = Article.objects.all()
        return context


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return redirect('index')


def about(request):
    return render(request, "about.html")