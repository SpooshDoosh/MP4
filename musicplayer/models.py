from django.db import models

# Create your models here.


class MusicPlayer(models.Model):
    audio_file = models.FileField(upload_to='music/', null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title
