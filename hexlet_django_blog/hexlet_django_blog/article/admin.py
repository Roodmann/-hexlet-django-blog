from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published_date",
    )  # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ["title", "content"]
    list_filter = (
        ("published_date", DateFieldListFilter),
    )   # Перечисляем поля для фильтрации
