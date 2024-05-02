# ecoimpact/urls.py
from django.contrib import admin
from django.urls import path, include
from user import views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .views import after_login_view

from .views import schedule_pickup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),

    path('about/', views.about_view),
    path('contact/', views.contact_view),

    path('adminclick/', views.adminClick_view),
    path('userclick/', views.userClick_view),

    path('adminsignup/', views.admin_signup_view),  
    path('adminlogin/', LoginView.as_view(template_name='adminlogin.html', success_url=reverse_lazy('landing_page')), name='admin_login'),

    path('aboutus/', views.about_us_view, name='about_us'),
    path('learn/', views.learn_view, name='learn'),
    
    path('after_login/', views.after_login_view, name='after_login'),

 

    path('schedule_pickup/', schedule_pickup_view, name='schedule_pickup'),


]
