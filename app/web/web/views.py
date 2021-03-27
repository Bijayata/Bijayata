from django.http import HttpResponse
# def index(request):
#     return HttpResponse("hello")


def index(request):
    return HttpResponse('''name<a href="https://docs.djangoproject.com/en/3.1/intro/tutorial01/">helo</a>''')
