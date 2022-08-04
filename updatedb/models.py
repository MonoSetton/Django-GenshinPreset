from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    weapon = models.CharField(max_length=50)
    vision = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artifact_set(models.Model):
    name = models.CharField(max_length=250)
    piece_2 = models.CharField(max_length=100)
    piece_4 = models.TextField()


class Weapons(models.Model):
    name = models.CharField(max_length=50)
    atk = models.CharField(max_length=15)
    stat = models.CharField(max_length=50)
    ability = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Sword(Weapons):
    pass


class Claymore(Weapons):
    pass


class Polearm(Weapons):
    pass


class Catalyst(Weapons):
    pass


class Bow(Weapons):
    pass

