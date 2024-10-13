from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from requests import request
import requests
from django.core.mail import send_mail
from .automailsender import send_automail
from django.conf import settings
from .models import *
from decouple import config
import os,datetime,random,string,json,time



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip_info(ip_address):
    api_token = config("IPINFO_API_KEY")
    url = f'https://ipinfo.io/{ip_address}/json?token={api_token}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def user_info(request,s):
    ip = get_client_ip(request)
    ip_info = get_ip_info(ip)
    
    if ip_info:
        ip_instance = IPInfo.objects.create(
            ip_address=ip,
            city=ip_info.get('city'),
            region=ip_info.get('region'),
            country=ip_info.get('country'),
            org=ip_info.get('org'),
            page=s,
        )
        ip_instance.save()
        return True
    else:
        return False

def home(request):
    #n = user_info(request,"home")
    if request.method == "POST":
        instance = AdminInquiry.objects.create(name=request.POST.get("name"),contact=request.POST.get("contact"),msg=request.POST.get("msg"))
        instance.save()
        if '@' in request.POST.get("contact"):
            subject = "Auto-response(noreply)"
            body= "We have received your inquiry. Thank you for your interest. Our response team will contact with you shortly."
            send_automail(to_email=request.POST.get("contact"),subject=subject,body=body)
            return redirect("home",{"message":"Your message has been sent",})
        else:
            return redirect("home",{"message":"Thank you for yur interest. Response team will contact with you shortly",})
    context = {}
    return render(request, "main/index.html",context)

def products(request):
    #n = user_info(request,"products")
    return render(request, "main/products.html")

def r_d(request):
    #n = user_info(request,"r_d")
    return render(request, "main/r_d.html")

def about(request):
    #n = user_info(request,"about")
    return render(request, "main/about.html")

def terms(request):
    #n = user_info(request,"terms")
    return render(request, "main/terms.html")

def privacy(request):
    #n = user_info(request,"privacy")
    return render(request, "main/privacy.html")

@staff_member_required
def admin_inquiry(request):
    inqs = AdminInquiry.objects.all().order_by("-id")
    context={
        "inqs":inqs,
    }
    return render(request,"main/admin-inquiry.html",context)

@staff_member_required
def site_log(request):
    logs = IPInfo.objects.all().order_by("-id")
    context = {
        'logs': logs[:100],
    }
    return render(request,"main/site-log.html",context)