from django.db import models

# Create your models here.
class Livre(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    page_number = models.IntegerField()
    editing_date = models.DateField(null=True, blank = True)
    summary=models.TextField()

