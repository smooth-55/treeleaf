from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    It stores the profile
    """

    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to="cv/")
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "profile"
        ordering = ["-id"]
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class SkillSet(models.Model):
    """
    It stores the skillsets for a profile
    """

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="skillset"
    )
    skill_name = models.CharField(max_length=40)
    proficiency_level = models.PositiveIntegerField()

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = "skillset"
        ordering = ["-id"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
