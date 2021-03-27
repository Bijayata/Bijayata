from _ast import Not

from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['user']
        pas = request.POST['pass']

        x = auth.authenticate(username=username1, password=pas)
        if x is not None:
            auth.login(request, x)
            return redirect('/')
        else:
            return redirect('login')

            # print('good')

    else:
        return render(request, 'login.html')
        # print('login')
