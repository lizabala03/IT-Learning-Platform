from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from home.models import Contact

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def course_view(request):
    return render(request,'course.html')

def free_course_view(request):
    return render(request,'free_course.html')

def paid_course_view(request):
    return render(request,'paid_course.html')

def profile_view(request):
    return render(request,'profile.html')

def dashboard_view(request):
    return render(request,'dashboard.html')

def help_view(request):
    if(request.method=='POST'):
        user_name = request.POST['user_name']
        email = request.POST['email']
        phn_number = request.POST['phn_number']
        comment = request.POST['comment']

        cnt = Contact(user_name=user_name,email=email,phn_number=phn_number,comment=comment)

        cnt.save()
        return redirect('Help and Contact')

    return render(request,'help.html')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['uname']
            pass1 = request.POST['psw']
            pass2 = request.POST['psw-repeat']
            if pass1 != pass2:
                messages.error(request,"Password didn't match!")
            else:
                myuser = User.objects.create_user(username=username, password=pass1)
                myuser.is_active=True
                myuser.save()
                return redirect('/login')
        return render(request,"signup.html")
    else:
        return redirect('/')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pws']
            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                messages.success(request, "LogIn Successfull")
                return redirect('/')

            else:
                messages.error(request, "username or password maybe incorrect")
                return redirect('/login')

        return render(request,'login.html')
    else:
        return redirect('/')

def logout_view(request):

    logout(request)
    return redirect('/')