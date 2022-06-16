from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"name": "Patrick", "age": 23, "nationality": 'British'}
    return render(request, "index.html", context=context)
