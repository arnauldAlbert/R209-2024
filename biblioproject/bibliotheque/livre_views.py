from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
from . import forms
# Create your views here

def ajout(request,id):
    lform= forms.LivreForm()
    categorie = models.Categorie.objects.get(pk=id)
    return render(request,"bibliotheque/livre/ajout.html",{"form":lform,"id":id,"categorie":categorie})

def traitement(request,id):
    lform=forms.LivreForm(request.POST)
    if lform.is_valid():
        livre=lform.save(commit=False)
        livre.categorie=models.Categorie.objects.get(pk=id)
        livre.save()
        resp=f"/bibliotheque/affiche/{id}/"
        return HttpResponseRedirect(resp)