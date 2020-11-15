from django.shortcuts import render
from .models import packagemodel
from .forms import applicants_form
from django.contrib import messages
# Create your views here.
def home(request):
    title="Home"
    return render(request,'core/home.html',{'title':title})

def available_packages(request):
    title="Packages"
    packages=packagemodel.objects.all()
    return render(request,'core/packages.html',{'title':title,'packages':packages})

def about_us(request):
    title="About Us"
    return render(request,'core/aboutus.html',{'title':title})


def contact_us(request):
    title="Contact Us"
    return render(request,'core/contactus.html',{'title':title})

def apply_now(request):
    title="Application"
    if request.method=="POST":
        fm=applicants_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You Have Successfully Applied For Training!!!')
    else:
        fm=applicants_form()
    return render(request,'core/apply.html',{'form':fm,'title':title})
