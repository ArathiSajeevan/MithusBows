from django.shortcuts import render, HttpResponse,redirect
from .forms import *
from .models import *
import uuid
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request,'index.html')

#load login page
def loadloginform(request):
    return render(request,'login.html')

#registration
def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            cn = a.cleaned_data['contact']
            pas = a.cleaned_data['password']
            cpas = a.cleaned_data['cpassword']

            if pas == cpas:
                b = regmodel(name=nm,email=em,contact=cn,password=pas)
                b.save()
                # return HttpResponse("Successfully Registered...")
                return redirect(login)
            else:
                return HttpResponse("Password and cpassword not match!")
        else:
            return HttpResponse("Enter valid data")
    return render(request,'register.html')

#login page
def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            pas = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                if em==i.email and pas==i.password:
                    id = i.id
                    nm = i.name
                    em = i.email
                    cn = i.contact
                    pas = i.password
                    return render(request,'index.html',{'id':id,'nm':nm,'em':em,'cn':cn,'pas':pas})
            else:
                return HttpResponse("Email and password incorrect..!")
        else:
            return HttpResponse("Please enter valid data")
    else:
        return render(request,'login.html')

def adminlogin(request):
    global User;
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect(adminlogin)
        profile_obj = adminregmodel.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check your email')
            return redirect(adminlogin)
        User = authenticate(username=username, password=password)

        if User is None:
            messages.success(request, 'wrong password or username')
            return redirect(adminlogin)
        # return HttpResponse('success')
        # for displaying registered user's username and email id
        # username = profile_obj.user.username
        # email = profile_obj.user.email
        # id = profile_obj.id
        return render(request, 'main.html') #main.html is the admin main page
    return render(request, 'adminlogin.html')

def adminregister(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        uname = request.POST.get('username')
        if password == cpassword:
            if User.objects.filter(username=uname).first():
                messages.success(request,"username already taken")
                return redirect(adminregister)

            if User.objects.filter(email=email).first():
                messages.success(request,"email already taken")
                return redirect(adminregister)

            user_obj=User(email=email,username=uname)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            profile_obj = adminregmodel.objects.create(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_regis(email, auth_token)
            return HttpResponse("Success")
            # return redirect(adminlogin)
    return render(request,'adminregister.html')


def send_mail_regis(email,token):
    subject = "your account has been verified"
    message = f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'

    email_from=EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    profile_obj = adminregmodel.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,"your account already verified")
            redirect(adminlogin)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request,"your account verified")
        return redirect(adminlogin)

    else:
        return redirect(error)

def error(request):
    return render(request,'error.html')

#admin main page
def main(request):
    return render(request,'main.html')

#add new item
def additem(request):
    if request.method == 'POST':
        a = itemform(request.POST,request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['itemname']
            des = a.cleaned_data['description']
            pr = a.cleaned_data['price']
            img = a.cleaned_data['image']
            b = item(itemname=nm,description=des,price=pr,image=img)
            b.save()
            return HttpResponse("Item added successfully")
        else:
            return HttpResponse("Failed")
    return render(request,'additem.html')


#display items
def showitem(request):
    items = item.objects.all()
    img = []
    name = []
    des = []
    price = []
    id = []
    for i in items:
        path = i.image
        img.append(str(path).split("/")[-1])

        nm = i.itemname
        name.append(nm)

        desc = i.description
        des.append(desc)

        pr = i.price
        price.append(pr)

        ids = i.id
        id.append(ids)
    mylist = zip(img,name,des,price,id)
    return render(request,'showitem.html',{'item':mylist})

def viewitem(request):
    items = item.objects.all()
    img = []
    name = []
    des = []
    price = []
    id = []
    for i in items:
        path = i.image
        img.append(str(path).split("/")[-1])

        nm = i.itemname
        name.append(nm)

        desc = i.description
        des.append(desc)

        pr = i.price
        price.append(pr)

        ids = i.id
        id.append(ids)
    mylist = zip(img,name,des,price,id)
    return render(request,'viewitem.html',{'item':mylist})

# def cart(request):
