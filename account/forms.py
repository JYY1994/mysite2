from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

#登录类
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

#注册表单类
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not match.')
        return cd['password2']

#注册表单 phone birth
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth',)

#个人信息数据类
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme','photo',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
