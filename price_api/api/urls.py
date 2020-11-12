from django.urls import path
from .views import users
from .views import collections

urlpatterns = [
    path("users/", users.Users.as_view()),
    path("collections/", collections.Collections.as_view()),
]
