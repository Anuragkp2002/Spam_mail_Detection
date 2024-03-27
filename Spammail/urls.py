"""
URL configuration for Spammail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views
from user import views as userviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('loginAction/',views.loginAction,name="loginAction"),
    path('addhobby/',views.addhobby,name="addhobby"),
    path('addhobbyAction/',views.addhobbyAction,name="addhobbyAction"),
    path("hobbyfactor/",views.hobbyfactor,name="hobbyfactor"),
    path("hobbyfactorAction/",views.hobbyfactorAction,name="hobbyfactorAction"),
    path('addseason/',views.addseason,name="addseason"),
    path('addseasonAction/',views.addseasonAction,name="addseasonAction"),
    path('addseasonfactor/',views.addseasonfactor,name="addseasonfactor"),
    path('addseasonfactorAction/',views.addseasonfactorAction,name="addseasonfactorAction"),
    path('registration/',userviews.registration,name="registration"),
    path('state/',userviews.state,name="state"),
    path('registrationAction/',userviews.registrationAction,name="registrationAction"),
    path('sendmessage/',userviews.sendmessage,name="sendmessage"),
    path('sendmessageAction/',userviews.sendmessageAction,name="sendmessageAction"),
    path('existing/',userviews.existing,name="existing"),
    path('viewsendmessage/',userviews.viewsendmessage,name="viewsendmessage"),
    path('delete<int:id>/',userviews.delete,name="delete"),
    path('viewreceivedmessage/',userviews.viewreceivedmessage,name="viewreceivedmessage"),
    path('viewreceivedmessageAction/',userviews.viewreceivedmessageAction,name="viewreceivedmessageAction"),
    path('viewtrash/',userviews.viewtrash,name="viewtrash"),
    path('Delete<int:id>/',userviews.Delete,name="Delete"),
    path('forward<int:id>/',userviews.forward,name="forward"),
    path('recieverexist/',userviews.recieverexist,name="recieverexist"),
    path('forwardAction/',userviews.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userviews.reply,name="reply"),
    path('replyAction/',userviews.replyAction,name="replyAction"),
    path('addcontact/',userviews.addcontact,name="addcontact"),
    path('contactexist/',userviews.contactexist,name="contactexist"),
    path('addcontactAction/',userviews.addcontactAction,name="addcontactAction"),
    path('blocklist/',userviews.blocklist,name="blocklist"),
    path('Contactexisting/',userviews.Contactexisting,name="Contactexisting"),
    path('blocklistAction/',userviews.blocklistAction,name="blocklistAction"),
    path('viewcontact/',userviews.viewcontact,name="viewcontact"),
    path('contactdelete<int:id>/',userviews.contactdelete,name="contactdelete"),
    path('viewcontactAction/',userviews.viewcontactAction,name="viewcontactAction"),
    path('viewblocklist/',userviews.viewblocklist,name="viewblocklist"),
    path('deleteblocklist<int:id>/',userviews.deleteblocklist,name="deleteblocklist"),
    path('addcustomerhobby/',userviews.addcustomerhobby,name="addcustomerhobby"),
    path('factor/',userviews.factor,name="factor"),
    path('customerhobbyAction/',userviews.customerhobbyAction,name="customerhobbyAction"),
    path('addseasoncountry/',views.addseasoncountry,name="addseasoncountry"),
    path('factors/',views.factors,name="factors"),
    path('getstates/',views.getstates,name="getstates"),
    path('SeasonAction/',views.SeasonAction,name="SeasonAction"),










    






    
]
