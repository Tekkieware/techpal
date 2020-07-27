from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.views import (LoginView, PasswordResetView, 
PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView,
PasswordChangeDoneView,LogoutView)
from django.views.generic import DetailView
from .forms import UserForm
from django.contrib.auth import get_user_model

# Create your views here.

class register(generic.edit.CreateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'account/register.html'
    success_url = '/account/login/'

class login(LoginView):
    template_name = 'account/login.html'

class passwordreset(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    success_url = '/account/password/reset/done'
class passwordresetdone(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class confirmpasswordreset(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = '/account/password-reset/complete'

class passwordresetcomplete(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

class PasswordChange(PasswordChangeView):
    template_name = 'account/password_change_form.html'
    success_url = '/account/password/change/done/'

class PasswordChangDone(PasswordChangeDoneView):
    template_name = 'account/passord_change_done.html'

class Logout(LogoutView):
    next_page = '/'
