from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from django.contrib.auth import login

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = 'index' 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)