from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('news/', views.newslist, name= 'news'),
    path('how-to/', views.howtolsit, name= 'how_to'),
    path('articles/', views.articlelist, name= 'articles'),
    path('entries/<int:pk>/<str:slug>', views.postdetail.as_view(), name= 'post'),
    path('<int:id>/<str:slug>/add-comment', views.comment, name= 'comment'),
    path('question/<str:user>', views.question, name= 'question'),

]