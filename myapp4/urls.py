from django.urls import path
from .views import user_form, many_fields_form

urlpatterns = [
    path("user/add", user_form, name="user_form"),
    path("user/many_add", many_fields_form, name="many_field_form")
]
