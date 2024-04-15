from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from . import models

class CategorieForm(ModelForm):
    class Meta:
        model=models.Categorie
        fields=('nom','description')
        labels = {"nom":_('Nom de la catégorie')}

class LivreForm(ModelForm):
            class Meta:
                model = models.Livre
                fields = ('title','author','page_number','editing_date','summary')
                labels={
                    "title":_("Titre"),
                    "author": _("Auteur"),
                    "page_number":_("Nombres de pages"),
                    "editing_date":_('Date de parution'),
                    "summary": _("Résumé")
                }
                localized_fields=("editing_date",)
                widgets={"editing_date": forms.TextInput(attrs={"type":"date"},)}

