from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sfedu_pass = models.CharField(max_length=50)
    sfedu_username = models.CharField(max_length=500, default='login')
    schadule = models.CharField(max_length=5000, default='empty')
    student_name = models.CharField(max_length=5000, default='empty')
    current_scores = models.CharField(max_length=5000, default='empty')
    current_max_scores = models.CharField(max_length=5000, default='empty')
    absolute_max_scores = models.CharField(max_length=5000, default='empty')
    student_info = models.CharField(max_length=5000, default='Введите учетные данные ЮФУ.')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Settings(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    url_of_notes = models.URLField(max_length=500, default='https://nimbusweb.me')
    url_of_disk = models.URLField(max_length=500, default='https://drive.google.com/drive/my-drive')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Settings.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.settings.save()

class Sidebar(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    name = models.CharField(default='Предмет', max_length=200)
    homework_link = models.URLField(max_length=500, default='#')
    aims_link = models.URLField(max_length=500, default='#')
    todo_link = models.URLField(max_length=500, default='#')


