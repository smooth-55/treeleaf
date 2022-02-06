from django.urls import path
from treeleaf.views import (
    ProfileCreateView,
    ProfileListView,
    RetrieveProfileView,
    ajax_skill_create,
    ajax_skill_update,
    DeleteProfile,
)

urlpatterns = [
    path("create", ProfileCreateView.as_view(), name="create"),
    path("", ProfileListView.as_view(), name="list"),
    path("view/<int:pk>/", RetrieveProfileView.as_view(), name="view"),
    path("delete/<int:pk>/", DeleteProfile.as_view(), name="delete"),
    path("skill/<int:pk>", ajax_skill_create, name="create-skill"),
    path("skill-update/<int:pk>", ajax_skill_update, name="update-skill"),
]
