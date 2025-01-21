from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):

  dest1 = Destination()
  dest1.name = 'Lagos'
  dest1.desc = 'Busy City'
  dest1.img = 'destination_1.jpg'
  dest1.price = 500
  dest1.offer = False

  dest2 = Destination()
  dest2.name = 'Ibadan'
  dest2.desc = 'Hotel City'
  dest2.img = 'destination_2.jpg'
  dest2.price = 400
  dest2.offer = True

  dest3 = Destination()
  dest3.name = 'Port Harcout'
  dest3.desc = 'Bole City'
  dest3.img = 'destination_3.jpg'
  dest3.price = 450
  dest3.offer = False

  dest4 = Destination()
  dest4.name = 'Owerri'
  dest4.desc = 'Hotel City'
  dest4.img = 'destination_2.jpg'
  dest4.price = 650
  dest4.offer = True


  dests = [dest1, dest2, dest3, dest4]

  
   
  return render(request,'index.html', {'dests': dests})  


