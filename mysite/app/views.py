from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request,"home.html",{'posts':posts})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form .is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,"registration/signup.html",{
        'form': form
    })

@login_required
def secret_page(request):
    return render(request, "secret_page.html")

class SecretPage(LoginRequiredMixin,TemplateView):
    template_name = "secret_page.html"

def add_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return render(request,'home.html')
    else:
        form = PostForm()
        return render(request,'post_form.html',{'form':form})

    