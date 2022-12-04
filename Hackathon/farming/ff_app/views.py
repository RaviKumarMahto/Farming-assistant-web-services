from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ff_app.models import Post,Comment
from ff_app.forms import PostForm,CommentForm
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# from httpresponse import httpresponse


# Create your views here.

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Already Exist')
                return redirect('blog:rg')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('blog:rg')
            else:
                user = User.objects.create_user(email=email,username=username,password=password)
                user.save()
                rec = [email]
                subject = "New Post Status"
                message = f" Hi {username} \n Thanks for Registering with out site \n Enjoy Farming"
                send_mail(subject,message,settings.EMAIL_HOST_USER,rec)
                return redirect('index')

        else:
            messages.info(request,'Password not maching')
            return redirect('blog:rg')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Username / Password incorrect')
            return redirect('index')
            
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def add_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request,'add_post.html',{'form':form})

    else:
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            body = form.cleaned_data['body']

            author = request.user

            post = Post(title=title,image=image,body=body,author=author)
            post.save()

            rec = [request.user.email]
            subject = "New Post Status"
            message = f" Hi {request.user.username} \n Thanks for adding a post \n Admin will review your post then Apperove"
            send_mail(subject,message,settings.EMAIL_HOST_USER,rec)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')


def changepassword(request):
    if request.method == "GET":
        ss = PasswordChangeForm(user=request.user)
        context={'abc':ss}
        return render(request,'changepass.html',context)

    elif request.method  == "POST":
        aa = PasswordChangeForm(user=request.user,data=request.POST)
        if aa.is_valid():
            userr=aa.save()
            update_session_auth_hash(request,userr)
            return redirect('home')
        
def blogs(request):
    return render(request, 'blogs.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def order_now(request):
    return render(request, 'order.html')