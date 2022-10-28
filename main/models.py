from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produce a signal if there is any database action.

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    occupation = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='pictures/image_profile/' , max_length=255, null=True, blank=True)
    def __str__(self):
        return "{0}".format(self.user.email)
        
# When any User instance created, Profile object instance is created automatically linked by User 
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
    else:
        instance.profile.save()