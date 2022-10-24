from os import name
from django.urls import path

app_name = "homepage"

from .views import (
    index,
    courses,
    raisec,
    courseDetails,
    recommendation,
    addGrade,
    contactPage
)

urlpatterns = [
    path('', index,name="homepage"),
    path('courses/',courses,name='courses'),
    path('raisec/',raisec,name="raisec"),
    path('course/details/<int:id>/',courseDetails,name="courseDetails"),
    path('recommendation/',recommendation,name="recommendation"),
    path('addGrade/',addGrade,name="addGrade"),
    path("contact/",contactPage,name="contact")
 
]