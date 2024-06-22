from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("public.urls"), name="public"),
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls"), name="dashboard"),
    path("sso/", include("sso.urls"), name="sso"),
]
