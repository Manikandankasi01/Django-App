from desg_t18.models import UserInformation
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model,login,logout
# from desg_t18.models import UserInforma

#UserInformation=get_user_model()
class UserRegistration(forms.ModelForm):
    user_name=forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=UserInformation
        fields ='__all__'

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('confirm_password')
        user_id=UserInformation.objects.filter(user_name=user_name)
        if user_id:
            raise ValidationError("User Already Exist !!")
            return user_id
        if password1 != password2:
            raise ValidationError("Password must be same !")
            return password1

class LoginForm(forms.ModelForm):
    user_name=forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=UserInformation
        fields=('user_name','password')

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        password = cleaned_data.get("password")
        db_pass=UserInformation.objects.filter(password=password)
        user_id=UserInformation.objects.filter(user_name=user_name)
        if not user_id:
            raise ValidationError("User Does not exist !!")
            return user_id
        if not db_pass:
            raise ValidationError("Invalid Credentials. Try Again !!")
            return password


class ResetForm(forms.ModelForm):
    user_name=forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=UserInformation
        fields =('user_name','password','confirm_password')
    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('confirm_password')
        user_id=UserInformation.objects.filter(user_name=user_name)
        if user_id:
            if password1 != password2:
                raise ValidationError("Password must be same !")
                return password1
        else:
            raise ValidationError("Invalid User name!!!")
            return user_id
        