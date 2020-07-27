from django.shortcuts import render,redirect
from .models import Post,Comment, Question
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    news = Post.objects.filter(post_type= 'News')[:7]
    articles = Post.objects.filter(post_type= 'Articles')[:7]
    howtos = Post.objects.filter(post_type= 'Howto')[:7]
    return render(request, 'blog/home.html', {'news':news, 'articles':articles, 'howtos':howtos})

def articlelist(request):
    post1 = Post.objects.filter(post_type = 'Articles').order_by("-hit_count_generic__hits").first()
    topposts = Post.objects.filter(post_type='Articles').order_by("-hit_count_generic__hits")[:3]
    posts_list = Post.objects.filter(post_type= 'Articles')
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'top_posts': topposts, 'posts': posts, 'title': 'Articles', 'post1':post1}
    return render(request, 'blog/posts.html', context)


def howtolsit(request):
    post1 = Post.objects.filter(post_type = 'Howto').order_by("-hit_count_generic__hits").first()
    topposts = Post.objects.filter(post_type='Howto').order_by("-hit_count_generic__hits")[:3]
    posts_list = Post.objects.filter(post_type= 'Howto')
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'top_posts': topposts, 'posts': posts, 'title': 'How To', 'post1':post1}
    return render(request, 'blog/posts.html', context)

def newslist(request):
    post1 = Post.objects.filter(post_type = 'News').order_by("-hit_count_generic__hits").first()
    topposts = Post.objects.filter(post_type='News').order_by("-hit_count_generic__hits")[:3]
    posts_lists = Post.objects.filter(post_type= 'News')
    paginator = Paginator(posts_lists, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'top_posts': topposts, 'posts': posts, 'title': 'Tech News', 'post1':post1}
    return render(request, 'blog/posts.html', context)

class postdetail(HitCountDetailView):
    model= Post
    template_name = 'blog/detail.html'
    context_object_name= 'post'
    count_hit = True

def comment(request, id, slug):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment = request.POST.get('coment')
            c = Comment(text = comment, post_id = id, user_id = request.user.id)
            c.save()
            return redirect(reverse('blog:post', args = [id, slug]))
    else:
        message = 'Sorry!!!!!. You have to login to be able to comment.'
        title = 'Login Required'
        return render(request, 'blog/message.html', {'message':message, 'title': title})

def question(request, user):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST.get('question')
            q = Question(text = question, user_id = request.user.id)
            q.save()
            message = 'Your Question was sent successfully!!!!!!!!. When there is an update, TechPAL will get back to you as soon as possible via Email'
            title = 'Guest Success Message'
            return render(request, 'blog/message.html', {'message':message, 'title': title})
    else:
        message = 'Sorry!!!!!. You have to login to be able to ask a quesion.'
        title = 'Login Required'
        return render(request, 'blog/message.html', {'message':message, 'title': title})