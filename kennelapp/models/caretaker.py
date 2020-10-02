from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .kennel import Kennel

class Caretaker (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Kennel, related_name="kennels",
        null=True,
        blank=True,
        on_delete=models.CASCADE)

# These receiver hooks allow you to continue to
# work with the `User` class in your Python code.

# Every time a `User` is created, a matching `Caretaker`
# object will be created and attached as a one-to-one
# property

    @receiver(post_save, sender=User)
    def create_caretaker(sender, instance, created, **kwargs):
        if created:
            Caretaker.objects.create(user=instance)

# Every time a `User` is saved, its matching `Caretaker`
# object will be saved.

    @receiver(post_save, sender=User)
    def save_caretaker(sender, instance, **kwargs):
        instance.caretaker.save()

    
