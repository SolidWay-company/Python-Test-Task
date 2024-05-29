from django.urls import path, include
from rest_framework import routers
from task.views import CategoreViewSet


router = routers.DefaultRouter()
router.register("categories", CategoreViewSet)


urlpatterns = [
    path(
        "", include(router.urls)
    ),
]

app_name = "task"
