from django.core.checks import messages
from django.http import HttpResponseGone, request
from django.shortcuts import render, redirect
from http.client import HTTPResponse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

from products.models import people


def login(request):

    if User.is_superuser == False:
        return redirect("/")

    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return render(request, "add.html")
            else:
                messages.info(request, "invalid username/password")
                return redirect("login")
        else:
            return render(request, "login.html")


def userlogin(request):
    pass


def register(request):

    try:
        if request.method == "POST":

            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]

            email = request.POST["email"]
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "User name already exist")
                    return redirect("register")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email is already exist")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password1,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    print("user created")
                    return redirect("login")
            else:
                messages.info(request, "Password not matching")
                return redirect("register")

            return redirect("/")

        else:
            return render(request, "register.html")
    except ValueError:
        print("user cannot be empty")
        return redirect("register")


def about(request):
    return render(request, "about.html")


def add(request):
    return render(request, "add.html")


def help(request):
    return render(request, "help.html")


def anouncement(request):
    return render(request, "anouncement.html")


def wherehouse(request):
    return render(request, "wherehouse.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


def details(request):
    if request.method == "POST":

        name = request.POST["name"]
        age = request.POST["age"]
        phone_number = request.POST["phone_number"]
        Aadhar_no = request.POST["Aadhar_no"]
        RD_NO = request.POST["RD_NO"]
        salary = request.POST["salary"]
        address = request.POST["address"]
        rationcard = request.POST["rationcard"]
        cardtype = request.POST["cardtype"]
        District = request.POST["District"]

        if people.objects.filter(Aadhar_no=Aadhar_no).exists():
            messages.info(request, "name already exist")
            return redirect("logout")
        elif people.objects.filter(rationcard=rationcard).exists():
            messages.info(request, "card is already exist")
            return redirect("logout")
        else:

            peoples = people(
                name=name,
                age=age,
                salary=salary,
                RD_NO=RD_NO,
                address=address,
                Aadhar_no=Aadhar_no,
                cardtype=cardtype,
                rationcard=rationcard,
                District=District,
                phone_number=phone_number,
            )

            peoples.save()
        messages.info(request, "details saved")
    return render(request, "logout.html")
