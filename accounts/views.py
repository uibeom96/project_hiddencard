from django.shortcuts import render, redirect
from accounts.forms import UserForm
from user.models import User


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            del(form.cleaned_data["password2"])
            User.objects.create_user(**form.cleaned_data)
            return redirect("main:index")
    else:
        form = UserForm()
    return render(request, "accounts/signup.html", {"form": form})