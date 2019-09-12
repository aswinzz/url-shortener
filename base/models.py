from django.db import models

# Create your models here.
class URL(models.Model):
    short=models.TextField(blank=False,null=False)
    url=models.TextField(blank=False,null=False)
    clicks=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now=True,blank=False,null=False)

