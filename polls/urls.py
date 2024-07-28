from django.urls import path

from . import views, image_api

urlpatterns = [
    path("", views.portfolio_page, name="home page"),
    path("foo/", views.bar, name="Test"),
    path("guzz/", views.upload_file, name="test upload"),
    path("shoot/", views.zoom, name="take a pic"),
    path("login-process/", views.try_login, name="login process"),
    path("auth/", views.auth, name="auth"),
    path("create-user/", views.try_sign_up, name="create user"),
    path("logout/", views.try_logout, name="logout"),
    path("display/", views.display, name="display"),
    path("view-photos/", views.view_photos, name="view photos ?"),
    path("show-photos/", views.show_photo, name="show photos"),
    path("does-the-user-exist/",
         views.does_the_user_exist,
         name="does the user exist"),
    path("success/", views.downloaded_page, name="success"),
    path("download-files/", views.download_files, name="download files"),
    path("home/", views.home, name="Portfolio"),
     path("post-review/", views.post_review, name="post review"),
     path("process/", image_api.process_image, name="peocess")
]
