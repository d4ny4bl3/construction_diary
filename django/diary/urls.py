from django.urls import path

from diary import views

urlpatterns = [
    path("projects/", views.create_project, name="create_project"),
]
