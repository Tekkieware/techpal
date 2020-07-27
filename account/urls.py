from . import views
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

app_name = 'account'

urlpatterns = [

    path('registration/' , views.register.as_view(), name = 'register'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('login/' , views.login.as_view(), name = 'login'),
    path('password/change/',views.PasswordChange.as_view(), name = 'password_change'),
    path('password/change/done/',views.PasswordChangDone.as_view(), name = 'password_change_done'),
    path('reset-password', views.passwordreset.as_view(), name = 'reset_password'),
    path('password/reset/done', views.passwordresetdone.as_view(), name = 'password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', views.confirmpasswordreset.as_view(), name = 'password_reset_confirm'),
    path('password-reset/complete', views.passwordresetcomplete.as_view(), name = 'password_reset_complete'),
]
