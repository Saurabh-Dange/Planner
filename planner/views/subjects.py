from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def add_subject(request):
    return render(request,'html/add_subject.html')