from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_year = models.PositiveSmallIntegerField(null=True)
    critic_rating = models.IntegerField(null=True)
    poster = models.URLField(null=True)
    mpaa_rating = models.CharField(max_length=100, null=True)
    runtime = models.PositiveIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    audience_score = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.title


class Favorite(models.Model):
    title = models.CharField(max_length=100, null=True)
    poster = models.URLField(null=True)
    identifier = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return self.title