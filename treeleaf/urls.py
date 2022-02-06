from django.urls import path
from treeleaf.views import (
    ProfileCreateView,
    ProfileListView,
    RetrieveProfileView,
    # CreateSkillView,
    ajax_skill_create,
    ajax_skill_update,
)

urlpatterns = [
    path("create", ProfileCreateView.as_view(), name="create"),
    path("", ProfileListView.as_view(), name="list"),
    path("view/<int:pk>/", RetrieveProfileView.as_view(), name="view"),
    # path("skill/<int:pk>", CreateSkillView.as_view(), name="create-skill"),
    path("skill/<int:pk>", ajax_skill_create, name="create-skill"),
    path("skill-update/<int:pk>", ajax_skill_update, name="update-skill"),
]
