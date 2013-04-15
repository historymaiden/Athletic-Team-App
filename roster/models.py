from django.db import models

# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=50)
    height = models.IntegerField(null=False, max_length=3)
    weight = models.IntegerField(null=False, max_length=3)
    class_level = models.CharField(max_length=20)
    primary_hand = models.CharField(max_length=20)
    hometown = models.CharField(max_length=50)
    high_school = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=50)
    parents = models.CharField(max_length=50)
    general = models.CharField(max_length=1000)
    junior_season = models.CharField(max_length=1000)
    sophomore_season = models.CharField(max_length=1000)
    freshman_season = models.CharField(max_length=2000)
    fall2012 = models.CharField(max_length=1000)
    prep_highlights = models.CharField(max_length=1000)
    image_uri = models.CharField(max_length=300)
    
    class Meta(object):
        ordering = ('name', 'pk')
    
    def __unicode__(self):
        return self.name
    
class Teams(models.Model): #for list of teams
    sport = models.CharField(unique=False, max_length=50) #the name of the sport
    coach = models.CharField(unique=False, max_length=50) #name of coach
    sportType = models.CharField(max_length=10) # men's or women's
    players = models.ManyToManyField("Player")
    class Meta(object):
        #verbose_name_plural = "List of Teams"
        ordering = ('sport', 'pk')
    
    def __unicode__(self):
        return self.sport
    
    def save(self, *args, **kwargs):
        self.sport = self.sport.upper()
        super(Teams, self).save(*args, **kwargs)
        

    
    
    
    