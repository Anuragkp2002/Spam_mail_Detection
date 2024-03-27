from django.contrib import messages
from django.shortcuts import render,redirect


from siteadmin.models import *
from user.models import *

# Create your views here.
def index(request):
    return render(request,'common/index.html')

def login(request):
    return render(request,'common/login.html')

def loginAction(request):
    Username=request.POST["username"]
    Password=request.POST["password"]
    siteadmin=admin_tb.objects.filter(Username=Username,Password=Password)
    user=register_tb.objects.filter(Username=Username,Password=Password)
    if siteadmin.count()>0:
        request.session['id']=siteadmin[0].id     
        messages.add_message(request,messages.INFO,'Login Succesfully')  
        return render(request,'admin/adminhome.html')
    elif user.count()>0:
        request.session['userid']=user[0].id
        messages.add_message(request,messages.INFO,'Login Succesfully')  
        return render(request,'user/userhome.html')
    else:
        messages.add_message(request,messages.INFO,'Login Failed')
        return redirect('login')
    
def addhobby(request):
    return render(request,'admin/addhobby.html')    

def addhobbyAction(request):
    Name=request.POST["hobby"]
    Hobby=hobbyname_tb(Hobbyname=Name)
    Hobby.save()
    return redirect('addhobby')

def hobbyfactor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,'admin/hobbyfactor.html',{'hb':hobby})

def hobbyfactorAction(request):
    Hobby=request.POST["hobby"]
    Factor=request.POST["factor"]
    Factorr=hobbyfactor_tb(Hobbyid_id=Hobby,Factorname=Factor)
    Factorr.save()
    messages.add_message(request,messages.INFO,'Factor Added')
    return redirect('hobbyfactor')

def addseason(request):
    return render(request,'admin/season.html')

def addseasonAction(request):
    Name=request.POST["season"]
    Season=season_tb(Seasonname=Name)
    Season.save()
    messages.add_message(request,messages.INFO,'Season Added')
    return redirect('addseason')

def addseasonfactor(request):
    factor=season_tb.objects.all()
    return render(request,'admin/seasonfactor.html',{'ft':factor})

def addseasonfactorAction(request):
    Season=request.POST["season"]
    Factors=request.POST["factor"]
    Fact=seasonfactor_tb(Seasonid_id=Season,Factorname=Factors)
    Fact.save()
    messages.add_message(request,messages.INFO,'Factor Added')
    return redirect('addseasonfactor')

    
def addseasoncountry(request):
    Season=season_tb.objects.all()
    Country=country_tb.objects.all()
    return render(request,'admin/addseason.html',{'sn':Season,'co':Country})



def factors(request):
    Snid=request.GET['sn'] 
    factor=seasonfactor_tb.objects.filter(Seasonid_id=Snid)
    return render(request,'admin/seasonfactors.html',{'ft':factor})  


def getstates(request):
    states=request.GET['ci']
    State=state_tb.objects.filter(Countryid_id=states)
    return render(request,'admin/getstates.html',{'st':State})  


def SeasonAction(request):
    Season=request.POST['season']
    Factor=request.POST['factor']
    Country=request.POST['country']
    State=request.POST['state']
    Month=request.POST['month']
    Season=seasoncountry_tb(Month=Month,Countryid_id=Country,Seasonfactorid_id=Factor,Seasonid_id=Season,Stateid_id=State)
    Season.save()
    messages.add_message(request,messages.INFO,"Added Successfully")
    return redirect('addseasoncountry')