from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from user.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
   user_level = Profile.objects.get(user=request.user)
   matric = user_level.matric_number
   school_check = All_students.objects.get(matric=matric)
   department = school_check.department
   level = school_check.level
   paid = school_check.paid
   total_unit = Registered_course.objects.filter(user=request.user).aggregate(Sum('reg_unit')).values()
   total_cost = Registered_course.objects.filter(user=request.user).aggregate(Sum('cost')).values()
   context = {

      "course_reg": Course.objects.filter(level=level, department=department),
      "level": level,
      "department": department,
      "matric": matric,
      "total_unit": total_unit,
      "total_cost": total_cost,
      "paid": paid,
      "broadcast": Broadcast.objects.filter(level=level, department=department),
      "all_message": Personal.objects.filter(receiver = request.user ),

      }
   return render(request, "index.html", context)
   
@login_required
def courses(request):
   user_level = Profile.objects.get(user=request.user)
   matric = user_level.matric_number
   school_check = All_students.objects.get(matric=matric)
   department = school_check.department
   level = school_check.level
   user_reg = Registered_course.objects.filter(user=request.user)

   context = {

      "course_reg": Course.objects.filter(level=level, department=department),
      "level": level,
      "department": department,
      "matric": matric,
      "added": Registered_course.objects.filter(user=request.user),

      }
   return render(request, "courses.html", context)

@login_required
def reg_course(request):
   if request.method == 'POST':
      user = request.user
      course_short = request.POST["course_short"]
      course_full = request.POST["course_full"]
      reg_unit = request.POST["unit"]
      cost = request.POST["cost"]
      course_regged = Registered_course.objects.filter(user=request.user,reg_course_short=course_short).exists()
      if course_regged is True:
         # message(request, 'You have previously registered for this course')
         return redirect('courses')
      else:
         details = Registered_course(user=user,reg_course_short=course_short,reg_course_full=course_full,reg_unit=reg_unit,cost=cost)
         details.save()
         return redirect('sem_courses')

   return render(request, "index.html")

@login_required
def sem_courses(request):
   user_level = Profile.objects.get(user=request.user)
   matric = user_level.matric_number
   school_check = All_students.objects.get(matric=matric)
   department = school_check.department
   level = school_check.level

   context = {

      "course_reg": Course.objects.filter(level=level, department=department),
      "level": level,
      "department": department,
      "matric": matric,
      "added": Registered_course.objects.filter(user=request.user),

      }
   return render(request, "regcourse.html", context)


@login_required
def user_message(request):
   if request.method == "POST":
      title = request.POST["title"]
      receiver = request.POST["to"]
      message = request.POST["message"]
      send = Personal(user=request.user, title=title, receiver=receiver, message=message)
      send.save()
      # message(request, 'Message sent successfully')
      return redirect('index')
   return render(request, "index.html")

@login_required
def paid(request):
   if request.method == "POST":
      paid = request.POST["paid"]
      user_level = Profile.objects.get(user=request.user)
      matric = user_level.matric_number
      update = All_students.objects.select_related().filter(matric=matric).update(paid=paid)
      # message(request, 'Message sent successfully')
      return redirect('index')
   return render(request, "index.html")