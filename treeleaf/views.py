from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from treeleaf.models import Profile

# Create your views here.


class ProfileListView(ListView):
    template_name = "treeleaf/profile-list.html"
    model = Profile


class RetrieveProfileView(DetailView):
    model = Profile
    template_name = "treeleaf/view-profile.html"


class ProfileCreateView(TemplateView):
    template_name = "treeleaf/profile-create.html"
