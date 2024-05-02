from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from user.forms import PickupSchedule

def index(request):
    return HttpResponse("<h1>This is my first Django page</h1>")

def home(request):
    context = {}
    return render(request, "index.html", context)

def contactus_view(request):
    return render(request, 'contact.html')

def landing_page_view(request):
    context = {}
    return render(request, 'landing_page.html', context)

# Modify the admin_login_view function to redirect to the landing page after successful login
def admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('landing_page_view')  # Redirect to landing page
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = AuthenticationForm()

    return render(request, 'adminlogin.html', {'form': form})

def after_login_view(request):
    print('jfdiujnvsf3fgv5dfsgvfsd5gv7fd7fd5cv login')
    
    return render(request, 'landing_page.html')

@login_required
def schedule_pickup_view(request):
    print('jfdiujnvsf3fgv5dfsgvfsd5gv7fd7fd5cv')
    if request.method == 'POST':
        form = PickupSchedule(request.POST)
        if form.is_valid():
            pickup_schedule = form.save(commit=False)
            pickup_schedule.user = request.user
            pickup_schedule.save()
            return render(request, 'pickup_confirmation.html', {'pickup_schedule': pickup_schedule})
    else:
        form = PickupSchedule()
    return render(request, 'schedule_pickup.html', {'form': form})
