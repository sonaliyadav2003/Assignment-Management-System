from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import datetime
#create connection from django to write manual queries
from django.db import connection

# Create your views here.


def index(request):
    return render(request,'user/index.html')
##########################################################
def about(request):
    return render(request,'user/about.html')

###############################################################

def contact(request):
    s=False
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('msg')
        contactInfo(Name=a,Email=b,Msg=d,Mobile=c).save()
        s=True
    return render(request,'user/contact.html',context={"msg":s})

##########################################################################

def signup(request):
    s=False
    if request.method=='POST':
      Name = request.POST.get('name')
      RNo= request.POST.get('rno')
      Mobile = request.POST.get('mob')
      Email= request.POST.get('email')
      Passwd= request.POST.get('passwd')
      Course=request.POST.get('course')
      Sem=request.POST.get('sem')
      Picture=request.FILES.get('ppic')
      asregster(name=Name,rno=RNo,mobile=Mobile,email=Email,passwd=Passwd,course=Course,year=Sem,pic=Picture).save()
      s=True

    mydict={"status":s}
    return render(request,'user/signup.html' ,context=mydict)

################################################################################

def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        currentuser=asregster.objects.filter(email=email,passwd=password)
        if currentuser:
            request.session['course']=str(currentuser[0].course)
            request.session['sem']=str(currentuser[0].year)
            request.session['name']=str(currentuser[0].name)
            request.session['pic']=str(currentuser[0].pic)
            request.session['user']=email

            return HttpResponse("<script>alert('Log in successfull');window.location.href='/user/index';</script>")
        else:
            return HttpResponse("<script>alert('Userid or password is incorrect');window.location.href='/user/signin';</script>")
    return render(request,'user/signin.html')

###################################################################################

def gallery(request):
    x = ugallery.objects.all().order_by('-id')#[0:6]
    mydict={"data":x}
    return render(request,'user/gallery.html',context=mydict)

################################################################################

def assignment(request):
    if request.session.get('user'):
        course=request.session.get('course')
        sem=request.session.get('sem')
        assignment=assignnmenttbl.objects.all().order_by('-id')
    else:
        return HttpResponse("<script>alert('Log in successfull');window.location.href='/user/signin';</script>")
    return render(request,'user/assignment.html',{'assignment':assignment})

#################################################################################

def assignmentdetails(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        user=request.session.get('user')
        if request.method=='POST':
            remark=request.POST.get('remark')
            afile=request.FILES.get('afile')
            studentanswer(sid=user, asid=id, sremark=remark, sanswer=afile, marks=0, submitdate=datetime.datetime.now()).save()
            return HttpResponse("<script>alert('Assignment submitted successfully');window.location.href='/user/assignmentdetails?id="+id+"';</script>")
        assignment = assignnmenttbl.objects.filter(id=id).order_by('-id')
        answer=studentanswer.objects.filter(sid=user,asid=id)
        return render(request, 'user/assignmentdetails.html', {'assignment': assignment,'answer':answer})
    return render(request,'user/assignmentdetails.html')
####################################################################################
def logout(request):

        del request.session['user']
        return render(request,'user/index.html')

##################################################################################

def profile(request):
    user=request.session.get('user')
    mydict={}
    if user:
       rdata=asregster.objects.all().filter(email=user)
       mydict={"rdata":rdata}
    return render(request, 'user/profile.html',mydict)
################################################################################

def lectures(request):
    a=request.GET.get('msg')
    ldata=lecturevideo.objects.all().filter(vcategory=a)
    md={"ldata":ldata}
    return render(request,'user/lectures.html',md)

####################################################

def lcategory(request):
    ldata=lecturecat.objects.all().order_by('-id')

    return render(request,'user/lcategory.html',{"ldata":ldata})

#############################################################

def viewlecture(request):
    return render(request,'user/viewlecture.html')




