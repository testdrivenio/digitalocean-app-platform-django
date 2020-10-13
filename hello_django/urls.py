from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def home(request):
    return JsonResponse({"hello": "world!"})


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
