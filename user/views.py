from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from elearn.models import *
from .forms import *



def index(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return HttpResponseRedirect(reverse('index'))
      else:
         return render(request, "login.html", {"message": "Invalid credentials."})
   return render(request, "login.html")


def logout_user(request):
   logout(request)
   return render(request, "login.html", {"message": "Logged out."})

def register(request):
   if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         matric = request.POST["matric"]
         prom = Profile.objects.filter(matric_number=matric).exists()
         if prom is True:
            return render(request, "register.html", {"message": "User have registered before"})
         user = form.save()
         department = request.POST["department"]
         user_profile = Profile(user=user, registered=True, department=department, matric_number=matric)
         user_profile.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('index')
      else:
         form = SignUpForm()
         return render(request, "register.html", {"message": "invalid data."})
   return render(request, 'register.html')

def validate_register(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(data)

def validate_matric(request):
    matric = request.GET.get('matric', None)
    # matric_check = All_students.objects.filter(matric=matric)
    matric_check = All_students.objects.filter(matric=matric).values('department')

    data = {

        'department': list(matric_check)
    }
    return JsonResponse(data)

def validate_message(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists(),
    }
    return JsonResponse(data)
