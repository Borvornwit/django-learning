from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"name": "Patrick", "age": 23, "nationality": "British"}
    return render(request, "index.html", context=context)


def counter(request):
    words = request.GET["words"]
    num_words = len(words.split())
    return render(request, "counter.html", {"num_words": num_words})
