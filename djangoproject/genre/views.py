from django.shortcuts import render
from django.http import HttpResponse
from . models import Collection,Piece
from django.views import generic

# Create your views here.
class index(generic.ListView):
    template_name = 'genre/genretemplate.html'

    def get_queryset(self):
        return Collection.objects.all()

class details(generic.DetailView):
    model= Collection
    template_name = "genre/detailtemplate.html"















#def index(request):
    #all_collection=Collection.objects.all()
    #context={
    #    "object_list" : all_collection
    #}
    #return render(request,"genre\\genretemplate.html",context)


#def details(request,genre_id):
    #Citem=Collection.objects.get(pk=genre_id)
    #Pitem=Piece.objects.filter(collection=Citem)
    #context={
    #    "Pitem" : Pitem
    #}

    #return render(request,"genre\\detailtemplate.html",context)