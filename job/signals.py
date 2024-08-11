from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def send_welcome_message(sender, instance: User, created, **kwargs):
    """Send welcome message to a new user"""
    if created:
        ...