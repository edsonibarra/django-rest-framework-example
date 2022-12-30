from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('courses', views.CourseViewset)

urlpatterns = [

    # localhost:8000/api/<path>/courses
    # In this case is an empty string so url results in localhost:8000/api/courses
    path("", include(router.urls)),
]
