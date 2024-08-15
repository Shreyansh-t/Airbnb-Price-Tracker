from django.shortcuts import redirect, render
from .scraper import start, open_site
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def home(request):

    start()
    open_site()
 
    return render(request, 'home.html')
    

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'welcome{username}')
            form.save()
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form})


# def login(request):

#     return render(request, 'login.html')
    