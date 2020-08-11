from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from testapp.models import *
from testapp.forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def order(request):
    if request.method=='POST':
        form=data_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=data_form()
    return render(request,'order.html',{'form':form})

def order_data(request):
    da=data.objects.all()
    return render(request,'orderdata.html',{'da':da})

# update function
def update(request,id):
    if request.method=='POST':
        id=data.objects.get(pk=id) # pk = primary key
        a=data_form(request.POST, instance=id)
        if a.is_valid():
            a.save()
            return redirect('orderdata')
    else:
        id=data.objects.get(pk=id) # pk = primary key
        a=data_form(instance=id)
    return render(request,'update.html',{'form':a})

# this function is used to delete data
def delete_data(request,id):
    if request.method=='POST':
        a=data.objects.get(pk=id) # pk = primary key
        a.delete()
        return redirect('add')

# login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid user and password')
            return redirect('login')
    else:
        return render(request,'base.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        if password==password1:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username is already taken')
               return redirect('signup')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'email is exists')
               return redirect('signup')
            else:
               user=User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
               user.save()
               return redirect('login')
        else:
           messages.info(request,'password is not matching')
           return redirect('signup')
        return redirect('/')
    else:
       return render(request,'base.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def contact(request):
    c1='WhatsApp No :8668769101'
    c2='Contact No : 8668769101'
    c3='imran pathan : 7498466580, 9130302617'
    c4='shoyeb shaikh : 8888454023'
    return render(request,'contact.html',{'c1':c1,'c2':c2, 'c3':c3, 'c4':c4})

def about(request):
    a='latur bazzar'
    return render(request,'about.html',{'a':a})

def feedback_views(request):
    display=feedback.objects.all()
    if request.method=='POST':
        form=feedback_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form=feedback_form()

    return render(request,'feedback.html',{'display':display,'form':form})
