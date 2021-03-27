from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def sinup(request):
    if request.method=='POST':
        username=request.POST['user']
        fnm=request.POST['fname']
        lnm=request.POST['lname']
        email=request.POST['email']
        pas= request.POST['pass']

        x=User.objects.create_user(username=username, first_name=fnm, last_name=lnm, email=email,
                                     password=pas)


        # print('user create')
        return redirect('/')


    else:
        return render(request,'bb.html')


# def sinup(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         first_name = request.POST['fname']
#         lastname = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['pass']
#
#         x = User.objects.create_user(username=username, first_name=first_name, last_name=lastname, email=email,
#                                      password=password),
#         # if x is not None:
#         #     auth.login(request,x)
#         #     return redirect('/')
#         # else:
#         #     return redirect('login')
#
#         print('user created')
#
#         return redirect('/')
#         # return render(request, 'b.html')
#
#     else:
#
#         return render(request, 'reg.html')
