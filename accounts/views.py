from typing import Generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate
from django.shortcuts import render
from .forms import SignUp


class SignUpView(generic.CreateView):
    form_class = SignUp
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    

class EditView(generic.UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user     







    
   

    