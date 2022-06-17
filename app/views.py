from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()

    return render(
        request,
        "index.html",
        {"features": features},
    )


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeat_password = request.POST["repeat_password"]

        if password == repeat_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password is not the same")
            return redirect("register")
    else:
        return render(request, "register.html")


# def counter(request):
#     words = request.POST["words"]
#     num_words = len(words.split())
#     return render(request, "counter.html", {"num_words": num_words})
