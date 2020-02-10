from django.shortcuts import render

from .models import Job


def home(requset):
    jobs = Job.objects

    return render(requset,'jobs/home.html',{'jobs':jobs})

