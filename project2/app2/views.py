from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app2.models import *
from .import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm





def registration_view(request):
    form=forms.RegistrationForm
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'Registration.html',{'form':form})


def home_view(request):
    return render(request,'home.html')


def attendance_view(request):
    return render( request,'attendance.html')


def about_view(request):
    return render( request,'about.html')

def coursedetails_view(request):
    return render( request,'coursedetails.html')

def Student_details_view(request):
    Student_list=Ignitz.objects.all()
    my_dict={'Student_list':Student_list}
    return render(request, 'student_details.html',context=my_dict)

def Attendance_details_view(request):
    Attendance_list=Attendance.objects.all()
    my_dict={'Attendance_list':Attendance_list}
    return render(request, 'Attendance_details.html',context=my_dict)


def Attendance_view(request):
    form=forms.AttendanceForm
    if request.method=="POST":
        form=forms.AttendanceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'attendance.html',{'form':form})




# def Login_view(request):
#     form=forms.LoginForm
#     if request.method=="POST":
#         form=forms.LoginForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)      
#     return render(request,'login.html',{'form':form})



# def Login_view(request):
#     if request.method == 'POST':
#         form =forms.LoginForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('Mail_Id')
#             password = request.POST.get('Password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('loginmain')
#             else:
#                 error_message = "Invalid login credentials"
#         else:
#             error_message = "Form is not valid"
#     else:
#         form = forms.LoginForm()
#         error_message = None

#     return render(request, 'login.html', {'form': form, 'error_message': error_message})


def Login_view(request):
    if request.method == 'POST':
        Mail_Id = request.POST.get('Mail_Id')
        password = request.POST.get('Password')

        try:
            user_profile = Login.objects.get(Mail_Id=Mail_Id)
        except Login.DoesNotExist:
            return HttpResponse("User does not exist.")

        if user_profile.password == password:
            return render(request, 'loginmain.html')
        else:
            return HttpResponse("Username or password is incorrect.")
    else:
        return render(request, 'loginmain.html')




# def Login_view(request):
#     if request.method == 'POST':
#         form =forms.LoginForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('Mail_Id')
#             password = request.POST.get('Password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('loginmain')
#             else:
#                 error_message = "Invalid login credentials"
#     return render(request, 'login.html')
@login_required
def loginmain_view(request):
    return render(request,'loginmain.html')








