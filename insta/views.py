from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,CommentsForm, ImageForm
from .email import send_welcome_email
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

def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
        return redirect('/')

    else:
        form = ImageForm()
        return render(request,'upload_image.html', {"form":form})

# @login_required (login_url='/accounts/register/')          
def image_likes(request,id):
    image =  Image.get_single_photo(id)
    user = request.user
    user_id = user.id
    
    if user.is_authenticated:
    
        image.save()
        
    return redirect('indexPage')

def add_comment(request,id):
    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
       
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('/')

    else:
        form = CommentsForm()
        return render(request,'add_comment.html',{"form":form,"image":image})  
    
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect ('profile')

    else:
        form = ProfileForm()
        return render(request,'django_registration/edit_profile.html',{"form":form})
    
    


def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('/')

    else:
        form = ImageForm()
    return render(request, 'new_post.html', {"form": form})

def delete_image(request,id):
    image = Image.objects.get(id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('/')
    return render(request, 'delete_post.html',{})





