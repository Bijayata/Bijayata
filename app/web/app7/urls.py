from.import views
from django.urls import path
from django.contrib import admin
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout',views.logout,name='logout'),
]
