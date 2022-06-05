from django.shortcuts import render
from vojaci.models import Rota, Stat, Osoba, Mesto, Ceta, Vyznamenani
from django.views.generic import ListView, DetailView


def index(request):
     """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""
     # Uložení celkového počtu filmů v databázi do proměnné num_films
     num_osoba = Osoba.objects.all().count()
     # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
     osoba = Osoba.objects.order_by('-hodnost')[:5]
     """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných 
    """
     context = {
     'num_osoba': num_osoba,
     'osoba': osoba
     }
     """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné 
    context k zobrazení """
     return render(request, 'index.html', context=context)


class VojaciListView(ListView):
     model = Osoba
     context_object_name = 'vojaci_list'
     template_name = 'osoba/list.html'


class VojaciDetailView(DetailView):
    model = Osoba
    context_object_name = 'vojaci_detail'
    template_name = 'osoba/detail.html'




