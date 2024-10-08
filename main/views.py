from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from requests import request
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from decouple import config
import os,datetime,random,string,json,time

def home(request):
    if request.method == "POST":
        instance = AdminInquiry.objects.create(name=request.POST.get("name"),contact=request.POST.get("email"),msg=request.POST.get("msg"))
        instance.save()
        context ={
            "message":"Your message has been sent",
        }
        return redirect("home")
    context = {}
    return render(request, "main/index.html",context)

def products(request):
    return render(request, "main/products.html")

def r_d(request):
    return render(request, "main/r_d.html")

def about(request):
    return render(request, "main/about.html")

@staff_member_required
def admin_inquiry(request):
    inqs = AdminInquiry.objects.all().order_by("-id")
    context={
        "inqs":inqs,
    }
    return render(request,"main/admin-inquiry.html",context)