from django.shortcuts import render, redirect
from travello.models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def destination(request):

  dests = Destination.objects.all()
  
  if request.user.is_authenticated:
     return render(request, 'destinations.html', {'dests': dests})
  else:
    return redirect('/accounts/login')
  