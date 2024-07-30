from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to='media/images/')
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Media(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images/')
    sub_title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class Even(models.Model):
    even = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.even

class Rapport(models.Model):  # Renommé de 'rapport' à 'Rapport'
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    action = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return self.title
