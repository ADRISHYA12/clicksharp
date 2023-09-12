from django.shortcuts import render,redirect
from userapp.models import registerdb,contactdb,appoitment
from clickapp.models import photogdb,saveitemdb,savecatdb,servicedb
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
def login(req):
    return render(req,"loginuser.html")
def logout(req):
    del req.session['Name']
    del req.session['Password']
    messages.success(req,"logout successfully")
    return redirect(login)

def register(req):
    return render(req,"register.html")
def savereg(req):
    if req.method == "POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        ph=req.POST.get('phone')
        pa=req.POST.get('password')
        obj=registerdb(Name=na,Mobile=ph,Email=em,Password=pa)
        obj.save()
        return redirect(login)

def loginfunction(req):
    if req.method =="POST":
        Na=req.POST.get('name')
        pa=req.POST.get('password')
        if registerdb.objects.filter(Name=Na,Password=pa).exists():
            req.session['Name']=Na
            req.session['Password']=pa
            messages.success(req,"login successfully")
            return redirect(home)
        else:
            messages.error(req,"invalid username or password")
            return redirect(login)
    else:
        messages.error(req,"invalid username or password")
        return redirect(login)

def home(req):
    data=servicedb.objects.all()
    pro=savecatdb.objects.all()
    bro=saveitemdb.objects.all()
    return render(req,"home.html",{'data':data,'pro':pro,'bro':bro})

def about(req):
    data=photogdb.objects.all()
    return render(req,"about.html",{'data':data})

def contact(req):
    return render(req,"contact.html")
def save_contact(req):
    if req.method == "POST":
        Na=req.POST.get('name')
        Em=req.POST.get('email')
        Mob=req.POST.get('mobile')
        Msg=req.POST.get('message')
        obj=contactdb(Name=Na,Email=Em,Mobile=Mob,Message=Msg)
        obj.save()
        messages.success(req,"MESSAGE HAS SENT OUR TEAM ")
        return redirect(contact)
def service(req):
    data=servicedb.objects.all()
    return render(req,"services.html",{'data':data})


def portfolio(req):
    data=saveitemdb.objects.all()
    return render(req,"portfolio.html",{'data':data})

def price(req):
    data=servicedb.objects.all()
    return render(req,"price.html",{'data':data})
def appoinment(req):
    data=servicedb.objects.all()
    return render(req,"appoinment.html",{'data':data})
def save_appoinment(req):
    if req.method == "POST":
        Na=req.POST.get('name')
        Em=req.POST.get('email')
        Mob=req.POST.get('mobile')
        dte=req.POST.get('date')
        ty=req.POST.get('type')
        tim=req.POST.get('time')
        Msg=req.POST.get('message')
        obj=appoitment(name=Na,email=Em,mobile=Mob,date=dte,typeofservice=ty,duration=tim,remarks=Msg)
        obj.save()
        messages.success(req,"YOUR APPOINMENT HAS BEEN APPROVED")
        return redirect(appoinment)

def singlephoto(req,catname):
    fafa=savecatdb.objects.all()
    data=saveitemdb.objects.filter(category_photo=catname)
    return render(req,"single photos.html",{'data':data})
def download(req,dataid):
    data=get_object_or_404(saveitemdb,id=dataid)
    response=HttpResponse(data.photo,content_type='image/jpeg')
    response['content-Disposition']=f'attachment;photo="{data.photo}"'
    return response










