from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

class SignUp(UserCreationForm):
  email = forms.EmailField()
  Address = forms.CharField(max_length = 100)

  class Meta:
      model = User
      fields =('username', 'email', 'password1', 'password2', 'Address')


class Edit(UserChangeForm):
  email = forms.EmailField()
  Address = forms.CharField(max_length = 100)

  class Meta:
      model = User
      fields =('username', 'email', 'Address')


  