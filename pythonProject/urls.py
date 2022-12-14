"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views as home_views
import home.views as course_views
import home.views as free_course_views
import home.views as paid_course_views
import home.views as profile_views
import home.views as dashboard_views
import home.views as help_views
import home.views as signup_views
import home.views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_view,name='Home'),
    path('course', course_views.course_view,name='Course'),
    path('free_course', free_course_views.free_course_view,name='Free-Course'),
    path('paid_course', paid_course_views.paid_course_view,name='Paid-Course'),
    path('profile', profile_views.profile_view,name='Profile'),
    path('dashboard/', dashboard_views.dashboard_view,name='Dashboard'),
    path('help/', help_views.help_view,name='Help and Contact'),
    path('signup/', signup_views.signup_view,name='SignUp'),
    path('login/', login_views.login_view, name='LogIn'),
    path('logout',home_views.logout_view),
]
