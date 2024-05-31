from django.contrib.auth import get_user_model  # type: ignore # noqa: F401
from django.db.models.signals import post_save  # type: ignore # noqa: F401
from django.dispatch import receiver  # type: ignore # noqa: F401
from authors.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(author=instance)
        profile.save()
