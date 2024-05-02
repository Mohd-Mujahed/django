from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import PickupSchedule

class AdminSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use. Please choose a different one.')
        return email

class PickupScheduleForm(forms.ModelForm):  # Renamed to PickupScheduleForm
    class Meta:
        model = PickupSchedule
        fields = ['name', 'address', 'phone', 'pickup_date', 'pickup_time']

# In your view function (schedule_pickup_view), use the form like this:

def after_login_view(request):
    print('hifdnjkvngfj',request)
    if request.method == 'POST':
        form = PickupScheduleForm(request.POST)  # Use PickupScheduleForm instead of PickupSchedule
        if form.is_valid():
            print(form.cleaned_data)  # Add this line for debugging
            # Rest of your code
    else:
        print('hifdnjkvngfj 123456789')
        
        form = PickupScheduleForm()

    # Rest of your view logic


