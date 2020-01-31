from django.db import models

# Create your models here.
class Activity(models.Model):
    #Dependent Variable y
    activity        =models.FloatField(null=True)
    #Variable X
    respiration     =models.FloatField()
    ECG             =models.FloatField()
    ACC_c_x         =models.FloatField()
    ACC_c_y         =models.FloatField()
    ACC_c_z         =models.FloatField()
    ACC_w_x         =models.FloatField()
    ACC_w_y         =models.FloatField()
    ACC_w_z         =models.FloatField()
    temperature     =models.FloatField()
    EDA             =models.FloatField()
    BVP             =models.FloatField()
    WEIGHT          =models.FloatField()
    Gender          =models.FloatField()
    AGE             =models.FloatField()
    SKIN            =models.FloatField()
    HEIGHT          =models.FloatField()
    SPORT           =models.FloatField()
    label           =models.FloatField()
    #Creation time
    created         =models.DateTimeField(auto_now_add=True)