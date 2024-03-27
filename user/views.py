import datetime
from turtle import update
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import siteadmin
from siteadmin.models import *

from user.models import *

# Create your views here.
def registration(request):
    Country=country_tb.objects.all()
    State=state_tb.objects.all()
    Hobby=hobbyname_tb.objects.all()
    return render(request,'user/register.html',{'cy':Country,'st':State,'hb':Hobby})

def state(request):
    cid=request.GET['co'] 
    state=state_tb.objects.filter(Countryid_id=cid)
    return render(request,'user/state.html',{'st':state})

def registrationAction(request):
    Name=request.POST["name"]
    Gender=request.POST["gender"]
    DOB=request.POST["dob"]
    Address=request.POST["address"]
    Country=request.POST["country"]
    State=request.POST["state"]
    Phone=request.POST["phonenumber"]
    Security=request.POST["security"]
    Answer=request.POST["answer"]
    Username=request.POST["username"]
    Password=request.POST["password"]
    Hobby=request.POST.getlist('checkbox')
    register=register_tb(Name=Name,Gender=Gender,DOB=DOB,Address=Address,CountryId_id=Country,StateId_id=State,Phonenumber=Phone,SecurityQuestion=Security,Answer=Answer,Username=Username,Password=Password)
    register.save()
    for hby in Hobby:
        hobbies=hobby_tb(Hobbyid_id=hby,Userid_id=register.id)
        hobbies.save()
        messages.add_message(request,messages.INFO,'Registration Succesfull')
    return redirect('registration')


def sendmessage(request):
    return render(request,'user/message.html') 

def sendmessageAction(request):
    Senderid=request.session['userid']
    Receiver=request.POST['receiver']
    Id=register_tb.objects.filter(Username=Receiver)
    rcvr=request.session['id']=Id[0].id    
    Subject=request.POST['subject']
    Message=request.POST['messages']
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    msg=message_tb(Senderid_id=Senderid,Receiverid_id=rcvr,Subject=Subject,Message=Message,Date=Date,Time=Time)
    msg.save()
    messages.add_message(request,messages.INFO,'Message sent Succesfully')
    return redirect('sendmessage')



def existing(request):
    Username=request.GET['user']
    user=register_tb.objects.filter(Username=Username)
    if user.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})

def viewsendmessage(request):
    Id=request.session["userid"]
    view=message_tb.objects.filter(Senderid_id=Id)
    return render(request,'user/viewsendmessage.html',{'vw':view})

def delete(request,id):
    message=message_tb.objects.filter(id=id)
    status=message[0].Status
    if(status == 'Pending'):
        update=message_tb.objects.filter(id=id).update(Status='Deleted by Sender')
    return redirect('viewsendmessage')
def viewreceivedmessage(request):
    Id=request.session["userid"]
    rcvrview=message_tb.objects.filter(Receiverid_id=Id)
    return render(request,'user/receiverview.html',{'rw':rcvrview})


def viewreceivedmessageAction(request):
    Receiverid=request.session["id"]
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    Checkbox=request.POST.getlist("checkbox")
    for v in Checkbox:
        trash=bin_tb(Date=Date,Time=Time,Messageid_id=v,Receiverid_id=Receiverid)
        trash.save()
    messages.add_message(request,messages.INFO,'Message added to trash')
    return redirect('viewreceivedmessage')


def viewtrash(request):
    trash=bin_tb.objects.all()
    return render(request,'user/viewtrash.html',{'tr':trash})


def Delete(request,id):
    message=message_tb.objects.filter(id=id)
    status=message[0].Status
    if(status == 'Pending'):
        update=message_tb.objects.filter(id=id).update(Status='Deleted by Receiver')
    elif(status == 'Deleted by Sender'):
        message.delete()
    return redirect('viewtrash')
def forward(request,id):
    forward=message_tb.objects.filter(id=id)
    return render(request,'user/forward.html',{'fw':forward})

def recieverexist(request):
    Username=request.GET['rcv']
    Receiver=register_tb.objects.filter(Username=Username)
    if Receiver.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})

def forwardAction(request):
    Senderid=request.session['userid']
    Receivername=request.POST['receivername']
    Id=register_tb.objects.filter(Username=Receivername)
    rcv=request.session['id']=Id[0].id  
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:") 
    Subject=request.POST['subject']
    Message=request.POST['message']
    frwrd=message_tb(Senderid_id=Senderid,Receiverid_id=rcv,Date=Date,Time=Time,Subject=Subject,Message=Message)
    frwrd.save()
    messages.add_message(request,messages.INFO,'Message Forwarded Successfully')
    return redirect('viewreceivedmessage')

def reply(request,id):
    reply=message_tb.objects.filter(id=id)
    return render(request,'user/reply.html',{'ry':reply})

def replyAction(request):
    Senderid=request.session['userid']
    Receivername=request.POST['name']
    Id=register_tb.objects.filter(Username=Receivername)
    Name=request.session['id']=Id[0].id 
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:") 
    Subject=request.POST['subject']
    Message=request.POST['message']
    Rply=message_tb(Senderid_id=Senderid,Receiverid_id=Name,Date=Date,Time=Time,Subject=Subject,Message=Message)
    Rply.save()
    messages.add_message(request,messages.INFO,'Reply sent Successfully')
    return redirect('viewreceivedmessage')


def addcontact(request):
    return render(request,'user/addcontact.html')

def contactexist(request):
    Username=request.GET['cntct']
    Contact=register_tb.objects.filter(Username=Username)
    if Contact.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})

def addcontactAction(request):
    Userid=request.session["userid"]
    Contactid=request.POST["contact"]
    Id=register_tb.objects.filter(Username=Contactid)
    Contactname=request.session['id']=Id[0].id 
    Name=request.POST["name"]
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    Remark=request.POST["remark"]
    Contact=contact_tb(Userid_id=Userid,Contactid_id=Contactname,Name=Name,Date=Date,Time=Time,Remarks=Remark)
    Contact.save()
    messages.add_message(request,messages.INFO,'Contact Added')
    return redirect('addcontact')


def blocklist(request):
    return render(request,'user/blocklist.html')

def Contactexisting(request):
    username=request.GET['ct']
    Contact=register_tb.objects.filter(Username=username)
    if Contact.count()>0:
        msg="exist"
    else:
        msg=" Not exist"
    return JsonResponse({'valid':msg})

def blocklistAction(request):
    Userid=request.session["userid"]
    Contactid=request.POST["contact"]
    Id=register_tb.objects.filter(Username=Contactid)
    Contactname=request.session['id']=Id[0].id 
    Name=request.POST["name"]
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M:")
    Remark=request.POST["remark"]
    Block=blocklist_tb(Userid_id=Userid,Contactid_id=Contactname,Name=Name,Date=Date,Time=Time,Remark=Remark)
    Block.save()
    messages.add_message(request,messages.INFO,'Blocklist Added')
    return redirect('blocklist')

def viewcontact(request):
    Contact=contact_tb.objects.all()
    return render(request,'user/viewcontact.html',{'ct':Contact})

def contactdelete(request,id):
    Deletecntct=contact_tb.objects.filter(id=id)
    Deletecntct.delete()
    messages.add_message(request,messages.INFO,"Contact Deleted")
    return redirect('viewcontact')

def viewcontactAction(request):
    Username=request.session["id"]
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime('%H:%M:')
    Checkbox=request.POST.getlist("chechbox")
    for v in Checkbox:
        Block=blocklist_tb(Userid_id=Username,Date=Date,Time=Time,Contactid_id=v)
        Block.save()
    return redirect('viewcontact')

def viewblocklist(request):
    Blck=blocklist_tb.objects.all()
    return render(request,'user/viewblocklist.html',{'bk':Blck})

def deleteblocklist(request,id):
    Del=blocklist_tb.objects.filter(id=id)
    Del.delete()
    messages.add_message(request,messages.INFO,"Contact Deleted")
    return redirect('viewblocklist')

def addcustomerhobby(request):
    Hobby=hobbyname_tb.objects.all()
    return render(request,'user/hobby.html',{'hb':Hobby})

def factor(request):
    hid=request.GET['hby'] 
    factor=hobbyfactor_tb.objects.filter(Hobbyid_id=hid)
    return render(request,'user/factor.html',{'fact':factor})

def customerhobbyAction(request):
    Userid=request.session['userid']
    Hobby=request.POST['hobby']
    Factor=request.POST['factor']
    HB=customerhobbyfactor_tb(Factorid_id=Factor,Hobbyid_id=Hobby,Userid_id=Userid)
    HB.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addcustomerhobby')