from django.urls import path

from diary.views import project_views

urlpatterns = [
    path("projects/statuses/", project_views.fetch_statuses, name="fetch_statuses"),

    path("projects/", project_views.fetch_projects, name="fetch_projects"),
    path("projects/add/", project_views.create_project, name="create_project"),
    path("projects/<int:project_id>/<slug:slug>/", project_views.fetch_project, name="fetch_project"),
    path("projects/<int:project_id>/<slug:slug>/edit/", project_views.update_project, name="update_project"),
]
