from accounts.views import login_view, logout_view, get_current_user

from django.urls import path


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("me/", get_current_user, name="get_current_user"),
]
