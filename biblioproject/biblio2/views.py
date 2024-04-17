from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from . import models
# Create your views here.
def ajout(request):
    lform = LivreForm()
    return render(request,"biblio2/ajout.html",{"form":lform})

def traitement(request):
    form = LivreForm(request.POST)
    if form.is_valid():
        livre= form.save()
        return HttpResponseRedirect("/biblio/index/")
    else:
        return render(request, "biblio2/ajout.html", {"form": form})

def all(request):
    liste=list(models.Livre.objects.all())
    return render(request,"biblio2/index.html",{"liste":liste})

def affiche(request,id):
    livre = models.Livre.objects.get(pk = id)
    return render(request, "biblio2/affiche.html", {"livre": livre})

def delete(request,id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/biblio/index/")

def update(request,id):
    livre = models.Livre.objects.get(pk=id)
    lform=LivreForm(livre.__dict__)
    return render(request, "biblio2/update.html", {"form": lform,"id":id})

def traitementupdate(request,id):
    form = LivreForm(request.POST)
    if form.is_valid():
        livre = form.save(commit=False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect("/biblio/index/")
    else:
        return render(request, "biblio2/ajout.html", {"form": form})