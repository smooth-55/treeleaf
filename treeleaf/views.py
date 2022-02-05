from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ProfileListView(TemplateView):
    template_name = "treeleaf/profile-list.html"


class RetrieveProfileView(TemplateView):
    template_name = "treeleaf/view-profile.html"


class ProfileCreateView(TemplateView):
    template_name = "treeleaf/profile-create.html"
