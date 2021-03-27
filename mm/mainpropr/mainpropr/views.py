from django.shortcuts import render
# Create your views here.
# def show(request):
#     return render(request,'index.html')

def index(request):
    return render(request,'homepage.html')
