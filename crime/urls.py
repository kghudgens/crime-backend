from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crimewatch import views
from users import views as userViews

router = routers.DefaultRouter()
router.register(r"post", views.PostView, "post")
router.register(r"profileview", userViews.ProfileView, "profileview")
router.register(r"userview", userViews.UserView, "userview")

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]
