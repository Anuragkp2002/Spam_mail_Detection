from django.db import models


# Create your models here.
class country_tb(models.Model):
    Countryname=models.CharField(max_length=20,default='')

class state_tb(models.Model):
    Countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    Statename=models.CharField(max_length=20)

class register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    CountryId=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    StateId=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    Phonenumber=models.CharField(max_length=20)
    SecurityQuestion=models.CharField(max_length=20)
    Answer=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class hobby_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)

class message_tb(models.Model):
    Senderid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Senderid')
    Subject=models.CharField(max_length=20)
    Message=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Receiverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,default='Pending')
    Filterstatus=models.CharField(max_length=20,default='Pending')

class bin_tb(models.Model):
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    Receiverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)

class contact_tb(models.Model):
    Contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Userid')
    Name=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=20)

class blocklist_tb(models.Model):
    Contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Contactid')
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Remark=models.CharField(max_length=20)

class customerhobbyfactor_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Hobbyid=models.ForeignKey("siteadmin.hobbyname_tb",on_delete=models.CASCADE)
    Factorid=models.ForeignKey("siteadmin.hobbyfactor_tb",on_delete=models.CASCADE)
