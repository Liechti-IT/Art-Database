from django.db import models

class Record(models.Model):
    img_title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    artist_name= models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    bild_art = models.CharField(max_length=50)
    bild_standort = models.CharField(max_length=50)
    Jahrgang = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)

