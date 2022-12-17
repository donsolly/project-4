from django.urls import path

from . import views

urlpatterns = [
   path("", views.index, name="login"),
   path("register/", views.register, name="register"),
   path("validate_register/", views.validate_register, name="validate_register"),
   path("validate_matric/", views.validate_matric, name="validate_matric"),
   path("validate_message/", views.validate_message, name="validate_message"),
   path("logout", views.logout_user, name="logout"),
]
