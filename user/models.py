from django.db import models

# Create your models here.
###########################################################
class contactInfo(models.Model):
    Name=models.CharField(max_length=80)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=40)
    Msg=models.TextField()
    def __str__(self):
        return self.Name
############################################################

class ugallery(models.Model):
    gdes=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='static/gallery/',default="")

########################################################################
class asregster(models.Model):
    rno=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    pic=models.ImageField(upload_to ='static/profile/',null=True)


##########################################################################################

class teacherreg(models.Model):
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    relcourse=models.CharField(max_length=100)
    profilepic=models.ImageField(upload_to='static/teacherpic',null=True)
    def __str__(self):
        return self.name

####################################################################

class assignnmenttbl(models.Model):
    atitle=models.CharField(max_length=200)
    adesc=models.TextField()
    course=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    asubject=models.CharField(max_length=100)
    assignby=models.ForeignKey(teacherreg,on_delete=models.CASCADE,null=True)
    assigndate=models.DateField()
    totalmarks=models.IntegerField()
    lastdate=models.DateField()
    status=models.CharField(max_length=20)
    attachfile=models.ImageField(upload_to='static/testfile/',null='True')

class studentanswer(models.Model):
    sid=models.CharField(max_length=100)
    asid=models.CharField(max_length=100)
    sremark=models.TextField()
    sanswer=models.ImageField(upload_to='static/answerfile/',null=True)
    marks=models.IntegerField()
    submitdate=models.DateField()
############################################

class lecturecat(models.Model):
    category=models.CharField(max_length=100)
    cpic=models.ImageField(upload_to='static/vcategory/',null=True)
    def __str__(self):
        return self.category

##############################################################################

class lecturevideo(models.Model):
    vlink=models.CharField(max_length=300)
    vtitle=models.CharField(max_length=200)
    vdes=models.TextField()
    vcategory=models.ForeignKey(lecturecat,on_delete=models.CASCADE, null=True)





















