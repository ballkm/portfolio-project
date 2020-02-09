from django.shortcuts import render

def home(requset):
    return render(requset,'jobs/home.html')

