from django import forms 
from django.forms import ModelForm
from .models import Article


class CommentArticleForm(forms.Form):
    content = forms.CharField(
        label="Комментарий",
        max_length=200,
        widget=forms.Textarea(attrs={
            'cols': 40,
            'rows': 10,
            'maxlength': 200,
            'required': True,
        })
    )


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.strip().lower() == "test":
            raise forms.ValidationError("Название не может быть 'test'")
        return name


class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data