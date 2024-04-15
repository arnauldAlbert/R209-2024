from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
from . import forms
# Create your views here.
def accueil(request):
    categories = models.Categorie.objects.all()
    return render(request,"bibliotheque/categorie/accueil.html",{"categories":categories})

def ajout(request):
    cform = forms.CategorieForm()
    return render(request,"bibliotheque/categorie/ajout.html",{"forms":cform})

def traitement(request):
    cform = forms.CategorieForm(request.POST)
    if cform.is_valid():
        c = cform.save()
        return HttpResponseRedirect("/bibliotheque/accueil/")
    else:
        return render(request, "bibliotheque/categorie/ajout.html", {"forms": cform})
def affiche(request, id):
    categorie = models.Categorie.objects.get(pk = id)
    livres=categorie.livre_set.all()
    return render(request,"bibliotheque/categorie/affiche.html",{"categorie": categorie, "livres":livres})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk = id)
    categorie.delete()
    return HttpResponseRedirect("/bibliotheque/accueil/")


def update(request,id):
    categorie = models.Categorie.objects.get(pk=id)
    cform = forms.CategorieForm(categorie.__dict__)
    return render(request, "bibliotheque/categorie/update.html", {"forms": cform, "id":id})

def traitementupdate(request,id):
    cform = forms.CategorieForm(request.POST)
    if cform.is_valid():
        c = cform.save(commit=False)
        c.id=id
        c.save()
        return HttpResponseRedirect("/bibliotheque/accueil/")
    else:
        return render(request, "bibliotheque/categorie/update.html", {"forms": cform, "id": id})
