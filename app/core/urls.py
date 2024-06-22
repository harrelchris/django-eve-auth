from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    path("sso/", include("sso.urls"), name="sso"),
]
