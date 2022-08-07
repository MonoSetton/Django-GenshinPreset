from django.db import models
from updatedb.models import Artifact_set
from django.contrib.auth.models import User


class Preset(models.Model):
    name = models.CharField(max_length=65, null=True, blank=False, default='Preset')
    first_stat = models.CharField(max_length=25, null=True)
    second_stat = models.CharField(max_length=25, null=True)
    third_stat = models.CharField(max_length=25, null=True)
    fourth_stat = models.CharField(max_length=25, null=True)
    fifth_stat = models.CharField(max_length=25, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Artifact(models.Model):
    STATUS = (
        ('bad', 'bad'),
        ('placeholder', 'placeholder'),
        ('good', 'good'),
    )
    set = models.ForeignKey(Artifact_set, on_delete=models.CASCADE, related_name='set')
    art = models.ForeignKey(Preset, on_delete=models.CASCADE, related_name='art', default=1)
    stat = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)