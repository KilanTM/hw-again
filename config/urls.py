
from app.views import hello_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("hello", hello_view),
    path("admin/", admin.site.urls),
]
