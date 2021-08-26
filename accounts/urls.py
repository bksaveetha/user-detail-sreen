from typing import Generic
from django.urls import path

from .views import EditView, SignUpView


urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/profile/', EditView.as_view(), name = 'profile'),
]



