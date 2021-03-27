from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# From covid import Covid
from covid import Covid

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("hello")
from requests import auth


def index(request):
    # return HttpResponse('''name<a href="https://docs.djangoproject.com/en/3.1/intro/tutorial01/">youtub</a>''')
    return render(request, 'index1.html')


# def profile(request):
#     return HttpResponse('hello profile')

def profile(request):
    return render(request, 'a.html', {
        'link': 'https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6'})


def jadoo(request):
    return render(request, 'b.html')


def exp(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a + b
    return render(request, 'output.html', {'result': c})


def covi(request):
    a = request.GET['text1']
    ovid = Covid()
    Cases = ovid.get_status_by_country_id(a)
    print(Cases)

    return render(request, 'output.html', {'result': Cases})


def sinup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        first_name = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']

        x = User.objects.create_user(username=username, first_name=first_name, last_name=lastname, email=email,
                                     password=password),
        # if x is not None:
        #     auth.login(request,x)
        #     return redirect('/')
        # else:
        #     return redirect('login')

        print('user created')

        return redirect('/')
        # return render(request, 'b.html')

    else:

        return render(request, 'reg.html')

        # print ("hello")
