# views.py
from django.shortcuts import render,redirect, reverse
from .forms import AdminSignupForm
from .import models, forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import PickupScheduleForm


def home_page_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def adminClick_view(request):
    return render(request, "adminClick.html")

def userClick_view(request):
    return render(request, "userClick.html")

def admin_signup_view(request):
    form = AdminSignupForm()
    print('hi')
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group, created = Group.objects.get_or_create(name='ADMIN')
            my_admin_group.user_set.add(user)
            return HttpResponseRedirect('/adminlogin/')
        else:
            print(form.errors)  # Print form errors for debugging
    return render(request, 'adminsignup.html', {'form': form})
def about_us_view(request):
    # Your view logic here, if needed
    return render(request, 'about.html')

def learn_view(request):
    # Your view logic here, you can add educational content, sources, researches, etc.
    return render(request, 'learn.html')


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
                return redirect('after_login_view')  # Redirect to after-login view
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = AuthenticationForm()

    return render(request, 'adminlogin.html', {'form': form})
@login_required
def schedule_pickup_view(request):
    print('Scheduling')
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pickup_date = request.POST.get('pickup_date')
        pickup_time = request.POST.get('pickup_time')

        # Validate form data if needed
        if not (name and address and phone and pickup_date and pickup_time):
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('schedule_pickup')  # Redirect back to the form page

        # Save pickup schedule to the database
        pickup_schedule = PickupScheduleForm.objects.create(
            name=name,
            address=address,
            phone=phone,
            pickup_date=pickup_date,
            pickup_time=pickup_time
        )

        # Optionally, you can associate the pickup schedule with the current user if you have user authentication
        # pickup_schedule.user = request.user
        # pickup_schedule.save()

        # Redirect to pickup confirmation page
        return redirect('pickup_confirmation')

    # If it's not a POST request, render the form page
    return render(request, 'schedule_pickup.html')
def after_login_view(request):
    print('Form submitted 12')

    if request.method == 'POST':
        print('Form submitted')
        form = PickupScheduleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Add this line for debugging
            # Process the form data here, e.g., save to the database
            form.save()
            # Redirect to a confirmation page or render a different template
            return redirect('/')
 # Replace 'confirmation_page' with the actual name of your confirmation page URL
    else:
        print('Form submitted 1234567890')
        
        form = PickupScheduleForm()

    return render(request, 'landing_page.html', {'form': form})
