from django.urls import path

from diary.views import project_views, material_views, daily_log_views

urlpatterns = [
    path("projects/statuses/", project_views.fetch_statuses, name="fetch_statuses"),

    path("projects/", project_views.fetch_projects, name="fetch_projects"),
    path("projects/add/", project_views.create_project, name="create_project"),
    path("projects/<int:project_id>/<slug:slug>/", project_views.fetch_project, name="fetch_project"),
    path("projects/<int:project_id>/<slug:slug>/edit/", project_views.update_project, name="update_project"),
    path("projects/<int:project_id>/<slug:slug>/delete/", project_views.delete_project, name="delete_project"),

    path("units/", material_views.fetch_units, name="fetch_units"),
    path("materials/", material_views.fetch_materials, name="fetch_materials"),
    path("materials/<int:material_id>/", material_views.fetch_material, name="fetch_material"),
    path("materials/add/", material_views.create_material, name="create_material"),
    path("materials/<int:material_id>/edit/", material_views.update_material, name="update_material"),
    path("materials/<int:material_id>/delete/", material_views.delete_material, name="delete_material"),

    path("purchases/", material_views.fetch_material_purchases, name="fetch_material_purchases"),
    path("purchases/add", material_views.create_material_purchase, name="create_material_purchase"),
    path("purchases/<int:purchase_id>/", material_views.fetch_material_purchase, name="fetch_material_purchase"),
    path("purchases/<int:purchase_id>/edit/", material_views.update_material_purchase, name="update_material_purchase"),
    path("purchases/<int:purchase_id>/delete/", material_views.delete_material_purchase, name="delete_material_purchase"),

    path("daily-logs/", daily_log_views.fetch_daily_logs, name="fetch_daily_logs"),
    path("daily-logs/add/", daily_log_views.create_daily_log, name="create_daily_log"),
    path("daily-logs/<int:daily_log_id>/", daily_log_views.fetch_daily_log, name="fetch_daily_log"),
    path("daily-logs/<int:daily_log_id>/edit/", daily_log_views.update_daily_log, name="update_daily_log"),
    path("daily-logs/<int:daily_log_id>/delete/", daily_log_views.delete_daily_log, name="delete_daily_log"),
]
