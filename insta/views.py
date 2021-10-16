from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,CommentsForm, ImageForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form =UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # messages.success(request,'Account was created successfully')
                return redirect('login')
        context = {'form': form}
        return render(request,'registration/registration_form.html',  context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            if user is not None:   
                login(request, user)
        context={'form': form}
        return render(request,'registration/login.html',  context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='/accounts/login/')
# def post(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.Author = current_user
#             post.save()
#         return redirect('loginPage')

#     else:
#         form = NewPostForm()
#     return render(request, 'post.html', {"form": form})

@login_required(login_url='login/')
def indexPage(request):
    images=Image.objects.all()
    comments=Comments.objects.all()
    profile = Profile.objects.all()
    return render(request,'index.html',{"images":images,"comments":comments, "profile":profile})

def profile(request):
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    posts =  request.user.image_set.all()
    return render(request,'django_registration/profile.html',{"images":posts,"profile":profile_info,"current_user":current_user})

def search_username(request):

    if 'search_username' in request.GET and request.GET["search_username"]:
        searched_name = request.GET.get("search_username")
        searched_user = User.objects.filter(username__icontains=search_username)
        message = f"{searched_name}"

        return render(request, 'search.html', {"message": message, "username": searched_name})

    else:
        message = "Sorry, No one by this username"
        return render(request, 'search.html', {"message": message})