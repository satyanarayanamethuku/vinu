from django.shortcuts import render,redirect
from .models import  ApplicationFormClass,Contact,Bhim_App,Quiz
import random
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


# Create your views here.

def application(request):
    if request.method=='POST':
        date = datetime.datetime.now()
        date1=datetime.datetime.strftime(date, "%Y-%m-%d")
        fname         = request.POST.get("fname")
        lname         = request.POST.get("lname")
        dob           = request.POST.get('dob')
        board         = request.POST.get('board')
        father        = request.POST.get("father")
        mother        = request.POST.get("mother")
        qualification = request.POST.get('qualification')
        sname         = request.POST.get('sname')
        saddress      = request.POST.get('Saddress')
        haddress      = request.POST.get('Haddress')
        state         = request.POST.get('state')
        anum          = request.POST.get('anum', '')
        phonenum      = request.POST.get('num')
        email         = request.POST.get('email')
        number        = '19'+'{:06d}'.format(random.randrange(1, 999999))
        username      = (state + board + qualification+ number)
        status        = request.POST.get('hidden1')
        referral      = request.POST.get('referral', '')
        if ApplicationFormClass.objects.filter(emailID=email).exists():
            messages.error(request,"Email ID Already Registered.Use Another One.")
        # elif status=='offline':
        #     af = ApplicationFormClass(firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, state = state, username = username, status=status, referral=referral)
        #     af.save()
        #     sub="Email From Best Scholarship"
        #     msg = "UserName:"+username+"."+"\n"+"password:"+str(dob)
        #     send_mail(sub,msg,'dontreply@ibest.co.in',[email])
        #     return HttpResponse('mail sent successfully')
        else:
            af = ApplicationFormClass(date=date1, firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, state = state, username = username, status=status, referral=referral)
            af.save()
            return redirect('/pay')
    return render(request, 'best/application.html')


def privacypolicy(request):
    return render(request, 'best/privacy.html')


def terms(request):
    return render(request, 'best/terms.html')

def refund(request):
    return render(request, 'best/refund.html')

def six(request):
    return render(request, 'best/six.html')


def home(request):
    return render(request, 'best/home.html')


def seven(request):
    return render(request, 'best/seven.html')


def eight(request):
    return render(request, 'best/eight.html')

def nine(request):
    return render(request, 'best/nine.html')


def ten(request):
    return render(request, 'best/ten.html')

def about(request):
    return render(request, 'best/about.html')


def update(request):
    return render(request, 'best/update.html')


def gallery(request):
    return render(request, 'best/gallery.html')

def brouchars(request):
    return render(request, 'best/brouchars.html')



def contact(request):
    if request.method == 'POST':
        name    =  request.POST.get('form_name')
        email   = request.POST.get('form_email')
        phone   = request.POST.get('form_phone')
        subject = request.POST.get('form_subject')
        message = request.POST.get('form_message')
        add=Contact(name = name, email=email, phone=phone, subject=subject, message=message)
        add.save()
        messages.success(request,"sucessfullu add details and we will contact get back soon")
    return render(request, 'best/contact.html')

def student_login(request):
    return render(request, 'best/studentlogin.html')

def admin_login(request):
    return render(request, 'best/adminlogin.html')

def payment(request):
    return render(request, 'best/pay.html')

def payment2(request):
    return render(request, 'best/payment.html')

def bhimapp(request):
    if request.method=='POST':
        tid   = request.POST['tid']
        tphn  = request.POST['tphn']
        email = request.POST['email']
        name  = request.POST['name']
        if ApplicationFormClass.objects.filter(emailID=email).exists():
            if Bhim_App.objects.filter(transactionid=tid).exists():
                messages.error(request,"Please Check Your Transaction Id")
                
            else:
                add=Bhim_App(transactionid=tid, phoneNumber=tphn, email=email, full_name=name)
                add.save()
                return HttpResponse("we will get back soon")
        else:
            messages.error(request,"please enter registered email id")
    return render(request, 'best/payment.html')


def student_profile(request):
    if request.method=='POST':
        request.session['name']=request.POST['uname']
        
        request.session['password']=request.POST['pwd']
        try:
            dbuser=ApplicationFormClass.objects.get(username=request.session['name'], date_of_birth=request.session['password'])
            if dbuser:
                return render(request, 'student/index.html',{"dbuser":dbuser})
            else:
                return HttpResponse("Login Fail")
        except ApplicationFormClass.DoesNotExist:
            messages.error(request, "username and passwod does not match")
            return render(request, 'best/studentlogin.html')
    return render(request, 'best/studentlogin.html')

def student_notification(request):
    try:
        username1 = request.session['name']
        dbuser=ApplicationFormClass.objects.get(username=username1)
    except:
        return render(request, 'best/studentlogin.html')

    return render(request, 'student/notification.html',{"dbuser":dbuser})


def student_mocktest(request):
    try:
        username1 = request.session['name']
        dbuser=ApplicationFormClass.objects.get(username=username1)
    except:
        return render(request, 'best/studentlogin.html')
    return render(request, 'student/mocktest.html', {"dbuser":dbuser})

def student_test(request):
    try:
        username1 = request.session['name']
        dbuser=ApplicationFormClass.objects.get(username=username1)
    except:
        return render(request, 'best/studentlogin.html')
    return render(request, 'student/test.html',{"dbuser":dbuser})


def student_logout(request):
    try:
        del request.session['name']

    except KeyError:
        pass

    return render(request, 'best/studentlogin.html')


def student_profile_view(request):
    try:
        username1 = request.session['name']
        dbuser=ApplicationFormClass.objects.get(username=username1)
    except:
        return render(request, 'best/studentlogin.html')
    return render(request, 'student/index.html',{"dbuser":dbuser})

def mail_sent(request, id):
    # if request.method=='POST':
        # email =request.POST['e1']
        email1=ApplicationFormClass.objects.get(id=id)
        # email2=Bhim_App.objects.get(email=email)
        sub="Email From Best Scholarship"
        msg = "UserName:"+email1.username+"."+"\n"+"password:"+str(email1.date_of_birth)

        # msg = "UserName:"+email1.username+"."+"\n"+"password:"+str(email1.date_of_birth)+"."+"\n"+"Transaction_Id:"+email2.transactionid
        send_mail(sub,msg,'dontreply@ibest.co.in',[email1.emailID])
     
        email1.mail_sent='mail sent'
        email1.save()
        return HttpResponse('mail sent successfully')
    # return render(request, 'best/emailsend.html')

def offline_register(request):
    return render(request, 'best/offline.html')

@login_required(login_url='/login/')
def index_view(request):
    return render(request,'admin12/index2.html')

@login_required(login_url='/login/')
def register_view(request):
    if request.method=='POST':
        userName=request.POST['username']
        email=request.POST['email']
        F_name=request.POST['f_name']
        L_name=request.POST['l_name']
        password=request.POST['pwd']
        if User.objects.filter(username=userName).exists():
            messages.info(request,'User name exist')
            return redirect('register')
        else:    
            user=User.objects.create_user(username=userName,email=email,first_name=F_name,last_name=L_name,password=password)
            user.save()
            return redirect('login')
    return render(request,'admin12/register.html')


def login_view(request):
    if request.method=='POST':
         userName=request.POST['username']
         password=request.POST['pwd']
         user=auth.authenticate(username=userName,password=password)
         if user:
             auth.login(request,user)
             return redirect('/index')
         else:
             messages.info(request,'invalid credential')
    return render(request,'admin12/login.html')

def logout_view(request):
    auth.logout(request)
    return render(request,'admin12/login.html')


def quiz(request):
    a=Quiz.objects.all()
    return render(request, 'admin12/a.html',{'b':a})

@login_required(login_url='/login/')
def student_profile_display(request):
    disp = ApplicationFormClass.objects.all()
    return render(request, 'admin12/studentprofile.html',{'disp':disp})

# @login_required(login_url='/login/')
# def studelete(request,id):
#     stu=ApplicationFormClass.objects.get(id=id)
#     stu.delete()
#     return redirect('/student_profile_display')



class StudentView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = ApplicationFormClass
    fields =['date', 'firstName','lastName', 'fatherName', 'motherName', 'schoolName', 'schoolAddress', 'homeAddress', 'referral', 'phoneNumber']
    template_name='admin12/applicationedit.html'


# if request.method=='POST':
#         fname         = request.POST.get("fname")
#         lname         = request.POST.get("lname")
#         dob           = request.POST.get('dob')
#         board         = request.POST.get('board')
#         father        = request.POST.get("father")
#         mother        = request.POST.get("mother")
#         qualification = request.POST.get('qualification')
#         sname         = request.POST.get('sname')
#         saddress      = request.POST.get('Saddress')
#         haddress      = request.POST.get('Haddress')
#         state         = request.POST.get('state')
#         anum          = request.POST.get('anum', '')
#         phonenum      = request.POST.get('num')
#         email         = request.POST.get('email')
#         number        = '19'+'{:06d}'.format(random.randrange(1, 999999))
#         username      = (state + board + qualification+ number)
#         status        = request.POST.get('hidden1')
#         referral      = request.POST.get('referral', '')
#         af = ApplicationFormClass(firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, state = state, username = username, status=status, referral=referral)
#         af.save()
#         messages.success(request, 'Student details upload sucessfully.')


def time(request):
    date = datetime.datetime.now()
    date1=datetime.datetime.strftime(date, "%Y-%m-%d")
    return HttpResponse(date1)

@login_required(login_url='/login/')
def admin_search_date(request):
    if request.method=='POST':
        date=request.POST['d1']
        add=ApplicationFormClass.objects.filter(date__iexact=date)
        return render(request, 'admin12/studentprofile.html',{'disp':add})
    return render(request, 'admin12/studentprofile.html')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model       = ApplicationFormClass
    context_object_name='b'
    template_name='admin12/applicationdelete.html'
    success_url = reverse_lazy('display_view')


# def Razorpay_Search(request):
#     pass


# def satya_request(request):
#     pass


@login_required(login_url='/login/')
def razorpay_search_date(request):
    if request.method=='POST':
        date=request.POST['e1']
        add=ApplicationFormClass.objects.filter(emailID__iexact=date)
        return render(request, 'admin12/studentprofile.html',{'disp':add})
    return render(request, 'admin12/studentprofile.html')


# def sandeep_view(request):
#     pass
