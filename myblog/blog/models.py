from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=170)
    content = models.TextField()
    metaDesc = models.CharField(max_length=170, default="")
    slug = models.CharField(max_length=70)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    is_published = models.BooleanField()

