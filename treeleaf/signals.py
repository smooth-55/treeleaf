from django.db.models.signals import pre_delete
from django.dispatch import receiver
from treeleaf.models import Profile


@receiver(pre_delete, sender=Profile)
def delete_related_skills(sender, instance, **kwargs):
    skill = instance.skillset.all()

    skill.delete()
