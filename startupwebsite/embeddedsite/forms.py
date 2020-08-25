from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class LoginForm(forms.Form):
    username = forms.CharField( 
        max_length=250, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
        
class RegistrationForm(forms.ModelForm):
    password =forms.CharField(label ='Password',widget =forms.PasswordInput())
    confirm_password =forms.CharField(label ='Confirm Password',widget =forms.PasswordInput())
    class Meta:
        model =User
        fields =['first_name','last_name','username','email',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','content']

class UserRegistration(UserCreationForm):
    """Customer registration."""
    username = forms.CharField(
        max_length=100, required=True, help_text='', label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    first_name = forms.CharField(
        max_length=100, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        max_length=100, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Second name'})
    )
    email = forms.EmailField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    
    password1 = forms.CharField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        max_length=250, required=True, help_text="", label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'})
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2',)
