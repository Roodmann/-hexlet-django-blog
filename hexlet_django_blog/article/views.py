from django.http import HttpResponse


def index(request):
    return HttpResponse("article")
# Create your views here.
