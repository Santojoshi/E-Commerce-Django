from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from app1.models import Customer    # To use model form for profile page

class register(UserCreationForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=(forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'})))

class profileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address', 'city', 'state', 'pin']
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}), 'address': forms.TextInput(attrs={'class':'form-control'}),
                   'city': forms.TextInput(attrs={'class':'form-control'}), 'state': forms.Select(attrs={'class':'form-control'}),
                   'pin': forms.NumberInput(attrs={'class':'form-control'})}