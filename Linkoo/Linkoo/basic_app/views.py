from django.shortcuts import render
from basic_app import models
from basic_app import forms
from django.http import HttpResponse
import pyqrcode
# Create your views here.

def home(request):

        return render(request, 'basic_app/home.html')




def register(request):
    
    form = forms.UserForm()
    
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return HttpResponse("Your URL is saved!")

    else:
        return render(request, 'basic_app/register.html', {'form':form})


def get_url(request):

        if request.method == 'POST':

                username = request.POST.get('username')
                key = request.POST.get('key')
                data = forms.User.objects.all()

                url = show_url(username, key, data) # Calling show_url function to get url from DB
                
                qrcode_gen(username)

                context = {
                        'username' : username,
                        'key' : key,
                        'url' : url
                        }
        return render(request, 'basic_app/final.html',  context)
       


def show_url(username, key, data):

        for entry in data:
                if entry.username == username and key == entry.key :
                        url = entry.url
                        return url
        return 'NOT FOUND'

def qrcode_gen(data):
        new = pyqrcode.create(data)
        new.png('static/qrcode/qrcode.png', scale = 5)