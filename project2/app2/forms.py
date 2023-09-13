from django import forms
from app2.models import Ignitz
from app2.models import Attendance
from app2.models import Login
from django.contrib.auth.forms import AuthenticationForm



class RegistrationForm(forms.ModelForm):


    class Meta:
        model=Ignitz
        fields='__all__'

        
class AttendanceForm(forms.ModelForm):

    class Meta:
        model=Attendance
        fields='__all__'


# class LoginForm(forms.ModelForm):

#     class Meta:
#         model=Login
#         fields='__all__'

class LoginForm(AuthenticationForm):
   
   class Meta:
        model=Login
        fields='__all__'



# class LoginForm(forms.Form):
#     Mail_Id = forms.EmailField()
#     Password = forms.CharField(max_length=100, widget=forms.PasswordInput)
