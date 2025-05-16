from django.urls import path

from diary import views

urlpatterns = [
    path("projects/statuses/", views.fetch_statuses, name="fetch_statuses"),
    path("projects/add/", views.create_project, name="create_project"),
    path("projects/<int:project_id>/<slug:slug>/", views.fetch_project, name="fetch_project"),
    path("projects/<int:project_id>/<slug:slug>/edit/", views.update_project, name="update_project"),
]
