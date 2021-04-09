from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def join(request):
    return render(request, '/join.html')

def dojoin(request):
    if request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        new_user = WebUser(user_id = id, user_pw = pw)
        new_user.save()
    return render(request, '/success.html')
