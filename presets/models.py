from django.db import models
from updatedb.models import Artifact_set, Character, Weapon
from django.contrib.auth.models import User


class Preset(models.Model):
    name = models.CharField(max_length=65, null=True, blank=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, default=1)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Artifact(models.Model):
    STATUS = (
        ('bad', 'bad'),
        ('placeholder', 'placeholder'),
        ('good', 'good'),
    )

    set = models.ForeignKey(Artifact_set, on_delete=models.CASCADE, blank=True, related_name='set')
    preset = models.ForeignKey(Preset, on_delete=models.CASCADE, related_name='preset', default=1)
    main = models.CharField(max_length=25, null=True, blank=True)
    first = models.CharField(max_length=25, null=True, blank=True)
    second = models.CharField(max_length=25, null=True, blank=True)
    third = models.CharField(max_length=25, null=True, blank=True)
    fourth = models.CharField(max_length=25, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.set

