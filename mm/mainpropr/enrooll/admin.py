from django.contrib import admin
from.models import student3

# Register your models here.
@admin.register(student3)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','address')
