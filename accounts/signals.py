from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwarg):
  print(created)
  if created:
    UserProfile.objects.create(user=instance)
    print('user profile is created')
  else:
    try:
      profile = UserProfile.objects.get(user=instance)
      profile.save()
    except:
      UserProfile.objects.create(user=instance)
      print('profile does not exist, but I created one')
      print('user is updated')

@receiver(pre_save, sender=User)
def pre_save_profile_receiveer(sender, instance, **kwargs):
  print(instance.username, 'this is being saved')