#This module/file is for communications between Models
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# receiver decorator will set signal event and the origin
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print(sender)
    # print(instance)
    # print(created)
    if created:
        Profile.objects.create(user=instance)
