from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Catégorie {self.nom}"

class Livre(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    page_number = models.IntegerField()
    editing_date=models.DateField()
    summary=models.TextField(null=True, blank=True)
    categorie=models.ForeignKey('categorie',on_delete=models.CASCADE)

    def __str__(self):
        return f"Livre {self.title} écrit par {self.author} de la catégorie {self.categorie}"