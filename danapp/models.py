from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Preferences(models.Model):
    colorChoices = (
        ('blue', 'blue'),
        ('red', 'red'),
        ('yellow', 'yellow'),
    )
    user = models.OneToOneField(User)
    colour = models.CharField(max_length=10, choices=colorChoices, default="Blue")
    font = models.CharField(max_length=100, blank = True, default="Times New Roman")
    picture = models.ImageField(upload_to='media',blank=True, default="/media/media/defaultim.jpg")