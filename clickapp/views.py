from django.shortcuts import render,redirect
from clickapp.models import photogdb,savecatdb,saveitemdb,servicedb,Event
from userapp.models import contactdb,appoitment
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    data=Event.objects.all()
    adrisya=contactdb.objects.all()
    cata=appoitment.objects.all()
    return render(request,'index.html',{'cata':cata,'adrisya':adrisya,'data':data})
def table(request):
    data=photogdb.objects.all()
    return render(request,'table.html',{'data':data})
def form(request):
    return render(request,'form.html')
def addphotographers(req):
    return render(req,"add photog.html")
def savephitod(req):
    if req.method=="POST":
        na=req.POST.get('name')
        de=req.POST.get('designation')
        im=req.FILES['photo']
        obj=photogdb(PNAME=na,PIM=im,desig=de)
        obj.save()
        return redirect(addphotographers)
def display(req):
    data=photogdb.objects.all()
    return render(req,"table.html",{'data':data})
def edit(req,dataid):
    data=photogdb.objects.get(id=dataid)
    return render(req,"edit.html",{'data':data})
def update(req,dataid):
    if req.method=="POST":
        na = req.POST.get('name')
        de = req.POST.get('designation')
        try:
            im=req.FILES['photo']
            fs=FileSystemStorage()
            FILE=fs.save(im.name,im)
        except MultiValueDictKeyError:
            FILE=photogdb.objects.get(id=dataid).PIM
        photogdb.objects.filter(id=dataid).update(PNAME=na,PIM=FILE,desig=de)
        return redirect(display)
def delete(req,dataid):
    data = photogdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)
def cat(request):
    return render(request,'category.html')
def savcat(req):
    if req.method=="POST":
        ca=req.POST.get('category')
        img=req.FILES.get['image']
        des=req.POST.get('description')
        obj=savecatdb(pcat=ca,pimg=img,pdes=des)
        obj.save()
        return redirect(cat)
def displaycat(req):
    data=savecatdb.objects.all()
    return render(req,"disply.html",{'data':data})
def editc(req,dataid):
    data=savecatdb.objects.get(id=dataid)
    return render(req,"editcat.html",{'data':data})
def updatec(req,dataid):
    if req.method=="POST":
        ca = req.POST.get('name')
        des = req.POST.get('decs')
        try:
            img = req.FILES['photo']
            fs=FileSystemStorage()
            FILE=fs.save(img.name,img)
        except MultiValueDictKeyError:
            FILE=savecatdb.objects.get(id=dataid).pimg
        savecatdb.objects.filter(id=dataid).update(pcat=ca,pimg=FILE,pdes=des)
        return redirect(displaycat)
def deletec(req, dataid):
        data = savecatdb.objects.filter(id=dataid)
        data.delete()
        return redirect(displaycat)
def single(req):
    data=savecatdb.objects.all()
    return render(req,"single page.html",{'data':data})

def saveitm(req):
    if req.method=="POST":
        cop=req.POST.get('catname')
        pn=req.POST.get('photo Name')
        ph=req.FILES['photo']
        des=req.POST.get('Description')
        obj=saveitemdb(category_photo=cop,photo_name=pn,photo=ph,p_description=des)
        obj.save()
        return redirect(single)
def display_single(req):
        data = saveitemdb.objects.all()
        return render(req, "displaysingle.html", {'data': data})
def edit_single(req,dataid):
    data=saveitemdb.objects.get(id=dataid)
    return render(req,"edit_single.html",{'data':data})
def updatesinglepage(req,dataid):
    if req.method=="POST":
        cop=req.POST.get('catname')
        pn=req.POST.get('photo Name')
        des=req.POST.get('description')
        try:
            img=req.FILES['photo']
            fs=FileSystemStorage()
            FILE=fs.save(img.name,img)
        except MultiValueDictKeyError:
            FILE=saveitemdb.objects.get(id=dataid).photo
        saveitemdb.objects.filter(id=dataid).update(category_photo=cop,photo_name=pn,p_description=des,photo=FILE)
        return redirect(display_single)
def delete_single(req, dataid):
        data = saveitemdb.objects.filter(id=dataid)
        data.delete()
        return redirect(display_single)
def add_service(req):
    return render(req,"add services.html")

def saveservice(req):
    if req.method=="POST":
        na=req.POST.get('name')
        de=req.POST.get('description')
        pr=req.POST.get('price')
        tm=req.POST.get('time')
        ty=req.POST.get('type')
        ph=req.FILES['photo']
        obj=servicedb(SNAME=na,SIM=ph,S_DESCRIPTION=de,price=pr,time=tm,type=ty)
        obj.save()
        return redirect(add_service)
def display_service(req):
    data=servicedb.objects.all()
    return render(req,"display service.html",{'data':data})
def edit_service(req,dataid):
    data=servicedb.objects.get(id=dataid)
    return render(req,"editservice.html",{'data':data})

def update_service(req,dataid):
    if req.method=="POST":
        na = req.POST.get('name')
        de=req.POST.get('description')
        pr=req.POST.get('price')
        tm=req.POST.get('time')
        ty=req.POST.get('type')
        try:
            im=req.FILES['photo']
            fs=FileSystemStorage()
            FILE=fs.save(im.name,im)
        except MultiValueDictKeyError:
            FILE=servicedb.objects.get(id=dataid).SIM
        servicedb.objects.filter(id=dataid).update(SNAME=na,S_DESCRIPTION=de,SIM=FILE,price=pr,time=tm,type=ty)
        return redirect(display_service)

def delete_service(req, dataid):
        data = servicedb.objects.filter(id=dataid)
        data.delete()
        return redirect(display_service)
def loginggpage(req):
    return render(req,"login.html")

def loginsucc(req):
    if req.method=="POST":
        un=req.POST.get('usne')
        pswd=req.POST.get('pswd')
        if User.objects.filter(username__contains=un,).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(req,user)
                req.session['username']=un
                req.session['password']=pswd
                return redirect(index)
            else:
                return redirect(loginggpage)
        else:
            return redirect(loginggpage)


def logoutadmin(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginggpage)
def display_contact(req):
    data=contactdb.objects.all()
    return render(req,"display contact.html",{'data':data})
def delete_contact(req, dataid):
        data = contactdb.objects.filter(id=dataid)
        data.delete()
        return redirect(display_contact)
def display_appoinment(req):
    data=appoitment.objects.all()
    return render(req,"display appoinment.html",{'data':data})
def delete_appoinment(req, dataid):
        data = appoitment.objects.filter(id=dataid)
        data.delete()
        return redirect(display_appoinment)
































