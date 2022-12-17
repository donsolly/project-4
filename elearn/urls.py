from django.urls import path

from . import views

urlpatterns = [
   path("dashboard", views.index, name="index"),
   path("courses", views.courses, name="courses"),
   path("reg_course", views.reg_course, name="reg_course"),
   path("sem_courses", views.sem_courses, name="sem_courses"),
   path("user_message", views.user_message, name="user_message"),
   path("paid", views.paid, name="paid"),
]
