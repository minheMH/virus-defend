from django.shortcuts import render

from . import models



def index(request):
    health = models.Healthstate.objects.all()
    return render(request,'virus-defend/index.html ',{'health':health})





