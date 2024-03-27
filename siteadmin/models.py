from django.db import models

# Create your models here.

class admin_tb(models.Model):
    Username=models.CharField(max_length=20,default='NULL')
    Password=models.CharField(max_length=20,default='NULL')
    
class hobbyname_tb(models.Model):
    Hobbyname=models.CharField(max_length=20)


class hobbyfactor_tb(models.Model):
    Hobbyid=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)
    Factorname=models.CharField(max_length=20)
    
class season_tb(models.Model):
    Seasonname=models.CharField(max_length=20)

class seasonfactor_tb(models.Model):
    Factorname=models.CharField(max_length=20)
    Seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)

class seasoncountry_tb(models.Model):
    Seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    Seasonfactorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    Countryid=models.ForeignKey("user.country_tb",on_delete=models.CASCADE)
    Stateid=models.ForeignKey("user.state_tb",on_delete=models.CASCADE)
    Month=models.CharField(max_length=20)