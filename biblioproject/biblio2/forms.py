from django import forms
from django.utils.translation import gettext_lazy as toto
from . import models

class LivreForm(forms.ModelForm):
    class Meta:
        model = models.Livre
        fields = ('title','author','editing_date','page_number','summary')
        # fields = ('__All__')
        labels ={
            "title":toto('Titre'),
            "author":toto('Auteur'),
            "editing_date":toto('Date de parution'),
            "page_number":toto("Nombre de pages"),
            "summary":toto("Résumé")
        }