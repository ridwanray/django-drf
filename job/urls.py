from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("about/", views.AboutView.as_view(), name="about_page"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("jobs/", views.JobListView.as_view(), name="login"),
]
