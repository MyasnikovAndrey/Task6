from django.shortcuts import render

from main.code.Neural_networks import NER
from main.code.SearchingTags import seatchTags


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def loading_page(request):
    text = request.GET['name']
    print(text)
    NER.ner(text)
    seatchTags.search_tags(text)
    print(seatchTags.tagPY)
    return render(request,'./loading_page.html', {'PY': seatchTags.tagPY, 'SQL': seatchTags.tagSQL,'DataS': seatchTags.tagDataS})

def abobus(request):
    return render(request,'./people.json')



