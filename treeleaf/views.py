from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from treeleaf.models import Profile, SkillSet

# Create your views here.


class ProfileListView(ListView):
    template_name = "treeleaf/profile-list.html"
    model = Profile


class RetrieveProfileView(DetailView):
    model = Profile
    template_name = "treeleaf/view-profile.html"


class ProfileCreateView(View):
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
        print("data saved")

        return redirect("/")
