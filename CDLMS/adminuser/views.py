from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from core.models import packagemodel,applicants_model
from .forms import package_form
from django.contrib import messages
# Create your views here.
def admin_login(request):
    usr=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(username=usr,password=pwd)
    if user:
        login(request,user)
        return JsonResponse({'status':1})
    return JsonResponse({'status':0})
    

def dashboard(request):
    page='Dashboard'
    if request.user.is_authenticated:
        users=applicants_model.objects.filter(status='Accept').count()
        new_applicants=applicants_model.objects.filter(status='Pending').count()
        packages=packagemodel.objects.all().count()
        return render(request,'adminuser/dashboard.html',{'page':page,'users':users,'packages':packages,'new_applicants':new_applicants})
    else:
        return HttpResponseRedirect('/')


def logout_admin(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    
def add_new_package(request):
    page='Add New Package'
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=package_form(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Package Successfully Added!!!')
        else:
            fm=package_form()
        return render(request,'adminuser/addpackage.html',{'form':fm,'page':page})
    else:
        return HttpResponseRedirect('/')

   
def manage_packages(request):
    page='Manage Packages'
    if request.user.is_authenticated:
        packages=packagemodel.objects.all()
        return render(request,'adminuser/packages.html',{'packages':packages,'page':page})
    else:
        return HttpResponseRedirect('/')

def update_package(request,id):
    page='Update Package'
    if request.user.is_authenticated:
        pi=packagemodel.objects.get(pk=id)
        if request.method=="POST":
            fm=package_form(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Package Updated Successfully !!!')
        else:
            fm=package_form(instance=pi)
        return render(request,'adminuser/addpackage.html',{'form':fm,'page':page})
    else:
        return HttpResponseRedirect('/')
    
def delete_package(request,id):
    if request.user.is_authenticated:
        pi=packagemodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/manage-packages/')
    else:
        return HttpResponseRedirect('/')


def new_applications(request):
    if request.user.is_authenticated:
        applications=applicants_model.objects.filter(status='Pending')
        return render(request,'adminuser/newapplications.html',{'applications':applications})
    else:
        return HttpResponseRedirect('/')

def view_applicant_detail(request,id):
    if request.user.is_authenticated:
        applicant=applicants_model.objects.get(pk=id)
        return render(request,'adminuser/viewapplicantdetail.html',{'applicant':applicant})
    else:
        return HttpResponseRedirect('/')

def take_action(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=applicants_model.objects.get(pk=id)
            pi.status=request.POST['status']
            pi.save()
            messages.success(request,'Done !!!!!')
            return HttpResponseRedirect('/adminuser/take-action/'+str(id)+'/')
        else:
            return render(request,'adminuser/takeaction.html',{'id':id})
    else:
        return HttpResponseRedirect('/')

def available_users(request):
    page="Available Users"
    if request.user.is_authenticated:
        applications=applicants_model.objects.filter(status='Accept')
        return render(request,'adminuser/availableusers.html',{'applications':applications,'page':page})
    else:
        return HttpResponseRedirect('/')
    

def available_user_detail(request,id):
    if request.user.is_authenticated:
        applicant=applicants_model.objects.get(pk=id)
        return render(request,'adminuser/availableuserdetail.html',{'applicant':applicant})
    else:
        return HttpResponseRedirect('/')