from django.urls import path
from treeleaf.views import ProfileCreateView, ProfileUpdateView, ProfileListView

urlpatterns = [
    path("create", ProfileCreateView.as_view(), name="create"),
    path("", ProfileListView.as_view(), name="list"),
    path("update", ProfileUpdateView.as_view(), name="update"),
]
