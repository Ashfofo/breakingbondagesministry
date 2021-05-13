from django.shortcuts import render


def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def contactus(request):
    return render(request,'contactus.html',{})

def visit(request):
    return render(request,'visit.html',{})

def donate(request):
    return render(request,'donate.html',{})

def partner(request):
    return render(request,'partnership.html',{})

def bio(request):
    return render(request,'prophetsuccess.html',{})

def index(request):
    return render(request,'index.html',{})