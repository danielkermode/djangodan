from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout

from danapp.forms import PreferenceForm
from danapp.models import Preferences


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            userc = form.save()
            pref = Preferences(user = userc)
            pref.save()
            if userc.is_active:
                gooduser = authenticate(username = request.POST['username'], password = request.POST['password1'])
                login(request, gooduser)
                return HttpResponseRedirect('/danapp/loggedin/')
            
            
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
    
def loginpage(request):
    stuffedup = False
    notactive = False
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        form = AuthenticationForm(request.POST)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/danapp/loggedin/')
            # Redirect to a success page.
            else:
               #user isnt active
                notactive = True
        else: 
            #form entry invalid
            stuffedup = True
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'stuffedup': stuffedup, 'notactive': notactive})

        
def loggedin(request):
    prefchanged = False
    colour="Blue"
    if not request.user.is_anonymous() :
        if request.user.is_authenticated:
            form = PreferenceForm()
            
            # when the user submits a form
            if request.method == 'POST':
                form = PreferenceForm(request.POST, request.FILES)
                if form.is_valid:
                    #registering preferences changes
                    p=Preferences.objects.get(user = request.user)
                    p.colour = request.POST.get('colour', p.colour)
                    p.font = request.POST.get('font', p.font)
                    p.picture = request.FILES.get('picture', p.picture)
                    p.save()
                    prefchanged = True
            
            preferences=Preferences.objects.get(user = request.user)
        return render(request,'loggedin.html',{'form': form, 'prefchanged': prefchanged,'preferences':preferences})
    else:
        return HttpResponseRedirect('/danapp/home/')
        
    
def home(request):
    if request.GET.get('register'):
        return HttpResponseRedirect('/danapp/register/')
    elif request.GET.get('login'):
        return HttpResponseRedirect('/danapp/login/')
    else:
        if not request.user.is_anonymous() :
            preferences=Preferences.objects.get(user = request.user)
            return render(request,'home.html',{'preferences':preferences})
        else:
            return render(request,'home.html')
def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/danapp/home/')
