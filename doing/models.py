from django.db import models
from account.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Planer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    task = models.TextField(null=True)
    


@receiver(post_save,sender=User)
def save_planer(sender,instance,created,**kwargs):
    if created:
        Planer.objects.create(user=instance) 