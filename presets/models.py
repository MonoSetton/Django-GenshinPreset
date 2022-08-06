from django.db import models
from updatedb.models import Artifact_set


class Artifact(models.Model):
    set = models.ForeignKey(Artifact_set, on_delete=models.CASCADE)
    main = models.CharField(max_length=25, null=True)
    first = models.CharField(max_length=25, null=True)
    second = models.CharField(max_length=25, null=True)
    third = models.CharField(max_length=25, null=True)
    fourth = models.CharField(max_length=25, null=True)


class Preset(models.Model):
    name = models.CharField(max_length=65)
    first_art = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name='first_art')
    second_art = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name='second_art')
    third_art = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name='third_art')
    fourth_art = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name='fourth_art')
    fifth_art = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name='fifth_art')

    def __str__(self):
        return self.name

