from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from django.views.generic.list import ListView
from treeleaf.models import Profile, SkillSet

# Create your views here.


class ProfileListView(ListView):
    """
    Profile list view
    """

    template_name = "treeleaf/profile-list.html"
    model = Profile


class RetrieveProfileView(DetailView):
    """
    Profile detail view
    """

    model = Profile
    template_name = "treeleaf/view-profile.html"


class ProfileCreateView(View):
    """
    It Creates the profile and skills with ajax from an asynchronous call
    """

    def get(self, request):
        context = {}
        return render(request, "treeleaf/profile-create.html", context)

    def post(self, request):

        full_name = request.POST["full_name"]
        email = request.POST["email"]
        skill = request.POST["skill"]
        level = request.POST["level"]
        photo = request.FILES.get("photo")
        cv = request.FILES.get("cv")

        create_profile = Profile.objects.create(
            name=full_name, email=email, cv=cv, photo=photo
        )

        SkillSet.objects.create(
            profile=create_profile, skill_name=skill, proficiency_level=level
        )

        return redirect("/")


class DeleteProfile(DeleteView):
    """
    It will delete user profile
    """

    model = Profile
    success_url = reverse_lazy("list")


def ajax_skill_create(request, pk):
    """
    It will create a skill for a profile with ajax
    """
    profile = Profile.objects.get(id=pk)

    skill_name = request.GET.get("skill")
    prof_level = request.GET.get("level")

    SkillSet.objects.create(
        profile=profile, skill_name=skill_name, proficiency_level=prof_level
    )

    return redirect("/")


def ajax_skill_update(request, pk):
    """
    It will update a skill for a profile with ajax
    """

    skill_name = request.GET.get("skill_name")
    prof_level = request.GET.get("proficiency_level")

    skill_object = SkillSet.objects.get(id=pk)
    skill_object.skill_name = skill_name
    skill_object.proficiency_level = prof_level
    skill_object.save()

    return redirect("/")
