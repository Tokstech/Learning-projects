from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']

    if password1 == password2:
      if User.objects.filter(username=username).exists():
        return render(request, 'register.html', {'error': 'Username not available'})

      elif User.objects.filter(email=email).exists():
        return render(request, 'register.html', {'error': 'Email Taken'})

      else:
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save();
        print ('user created')
        return redirect('/')
    else:
      print('password not matching...')
      return render(request, 'register.html', {'error': 'Passwords do not match!'})
    
  else:
    return render(request, 'register.html')