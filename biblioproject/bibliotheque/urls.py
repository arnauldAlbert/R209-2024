from django.urls import path

from . import categorie_views, livre_views

urlpatterns = [
    #urls des categories
    path('accueil/',categorie_views.accueil),
    path('ajout/', categorie_views.ajout),
    path('traitement/',categorie_views.traitement),
    path('affiche/<int:id>/', categorie_views.affiche),
    path('delete/<int:id>/',categorie_views.delete),
    path('update/<int:id>/', categorie_views.update),
    path('traitementupdate/<int:id>/', categorie_views.traitementupdate),

    # urls des Livres
    path('livreajout/<int:id>/',livre_views.ajout),
    path('livretraitement/<int:id>/',livre_views.traitement),
]