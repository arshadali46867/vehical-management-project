from django.contrib import admin

# Register your models here.
from .models import *


@admin.register( Customer)

class AdminProduct(admin.ModelAdmin):

    list_display=['id','profile_pic']




@admin.register( Mechanic)

class AdminProduct(admin.ModelAdmin):

    list_display=['id','profile_pic']
