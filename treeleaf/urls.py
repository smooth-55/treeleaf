from django.urls import path
from treeleaf.views import (
    ProfileCreateView,
    ProfileListView,
    RetrieveProfileView,
)

urlpatterns = [
    path("create", ProfileCreateView.as_view(), name="create"),
    path("", ProfileListView.as_view(), name="list"),
    path("view", RetrieveProfileView.as_view(), name="view"),
]
