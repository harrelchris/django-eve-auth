from django.urls import path

from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path(route="", view=views.IndexView.as_view(), name="index"),
]
