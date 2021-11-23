from django import forms
from zummitlabsdjango.models import UserProfileInfo
from django.contrib.auth.models import User


class UserfForm(forms.ModelForms):
    password = forms.charFiled(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


