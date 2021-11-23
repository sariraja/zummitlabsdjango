from django.shortcuts import render
from zummitlabsdjango.forms import UserForm,UserProfileInfoForm,
from django.contrib.auth import authenticate, login,logout
from django.https import HttpsResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'zummitlabsdjango/index.html')
@login_required()
def special(request):
    return HttpResponse("you are logged in !")

@login_required()
def user_logout