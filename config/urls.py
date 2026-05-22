from django.conf.urls.static import static
from django.urls import path

from authLesson import views

urlpatterns = [
    path("signup/", views.register_page, name="register_page"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_view, name="logout"),
    path("auth/", views.auth_page, name="auth_page"),
    path("newuser/", views.register_view, name="new_user"),
    path("login-view/", views.login_view, name="login_view"),
    path("create-user/", views.create_user, name="create_user"),
    path("create-manager/", views.create_manager, name="create_manager"),
    path("test/", views.test, name="test"),
]