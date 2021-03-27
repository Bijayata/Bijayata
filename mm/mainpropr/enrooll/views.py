from django.shortcuts import render
from .models import student3
from .import forms
from . forms import UserRegisterationForm
# Create your views here.
# def show(request):
#     return render(request,'index.html')

def show(request):
    stu=student3.objects.all()
    return render(request,'index.html',{'st':stu})
def sinup(request):
    return render(request,'index.html')

def signup(request):

    if request.method == 'POST':
        RegisterationForm = UserRegisterationForm(request.POST)

        if RegisterationForm.is_valid():
            RegisterationForm.cleaned_data['name']
            # RegisterationForm.cleaned_data['email']
            RegisterationForm.cleaned_data['address']

            RegisterationForm.save()
            RegisterationForm = UserRegisterationForm()
    else:
        RegisterationForm = UserRegisterationForm()

    return render(request, 'signup.html', {'form': RegisterationForm})

