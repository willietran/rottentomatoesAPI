from django.db import models

# Create your models here.


class Team(models.Model):
    type = models.CharField(max_length=30)

    def __unicode__(self):
        return u"{}".format(self.type)


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()
    pokedex_id = models.PositiveIntegerField()
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{}".format(self.name)