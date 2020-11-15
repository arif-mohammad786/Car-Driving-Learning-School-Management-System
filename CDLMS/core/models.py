from django.db import models

# Create your models here.
class packagemodel(models.Model):
    pname=models.CharField(max_length=255)
    pdesc=models.TextField()
    pduration=models.IntegerField()
    pprice=models.IntegerField()


class applicants_model(models.Model):
    packages=packagemodel.objects.all()
    choice1=[]
    for p in packages:
        choice1.append((p.pname,p.pname))
    choice2=[
        ('09:00AM-10:00AM','09:00AM-10:00AM'),('10:00AM-11:00AM','10:00AM-11:00AM'),('11:00AM-12:00PM','11:00AM-12:00PM'),
        ('12:00PM-01:00PM','12:00AM-01:00PM'),('01:00PM-02:00PM','01:00AM-02:00PM'),('02:00PM-03:00PM','02:00AM-03:00PM'),
        ('03:00PM-04:00PM','03:00AM-04:00PM'),('04:00PM-05:00PM','04:00AM-05:00PM'),('05:00PM-06:00PM','05:00AM-06:00PM'),
    ]
    choice3=[
        ('MALE','MALE'),('FEMALE','FEMALE'),('TRANSGENDER','TRANSGENDER')
    ]
    package=models.CharField(max_length=255,choices=choice1,default=choice1[0])
    start_date=models.DateField()
    timing=models.CharField(max_length=255,choices=choice2,default=choice2[0])
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=255,choices=choice3,default=choice3[0])
    age=models.IntegerField()
    licenseno=models.IntegerField() 
    licensepic=models.FileField()
    address=models.TextField() 
    status=models.CharField(max_length=255,default="Pending")  