from django.http import HttpResponse
from django.shortcuts import render

def task(request):
    data = {
        "title": "Internship Task 1 ",
        "tasks": ["Add Dynamic Data To html Page","Name - Nirdesh Tiwari "]
    }
    return render(request, "task.html", context=data)
def index(request):
    return render(request,"index.html")