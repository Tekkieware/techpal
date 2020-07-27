from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required= False)
    last_name = forms.CharField(max_length=30, required= False)
    email = forms.EmailField(max_length= 254, help_text= 'Required. Enter a valid email address.')

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()
      
        