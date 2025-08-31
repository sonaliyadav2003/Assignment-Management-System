from django.contrib import admin
from . models import *


class contactInfoAdmin(admin.ModelAdmin):
    list_display = ('Name','Mobile','Email','Msg')

admin.site.register(contactInfo,contactInfoAdmin)

#############################################
class ugalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gdes','picture')
admin.site.register(ugallery,ugalleryAdmin)

###############################################
class asregsterAdmin(admin.ModelAdmin):
    list_display=('rno','name','mobile','email','passwd','course','year','pic')
admin.site.register(asregster,asregsterAdmin)

###############################################################
class teacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','post','profilepic','relcourse')
admin.site.register(teacherreg,teacherAdmin)

################################################################
class assignmentAdmin(admin.ModelAdmin):
    list_display = ('id','atitle','adesc','course','semester','asubject','assignby','assigndate','totalmarks','lastdate','status','attachfile')
admin.site.register(assignnmenttbl,assignmentAdmin)

######################################################################################
class answerAdmin(admin.ModelAdmin):
    list_display = ('id','sid','asid','sremark','sanswer','marks','submitdate')
admin.site.register(studentanswer,answerAdmin)
####################################################
class lecturecatAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic')
admin.site.register(lecturecat,lecturecatAdmin)

############################################################

class lecturevideoAdmin(admin.ModelAdmin):
    list_display=('id','vtitle','vlink','vdes','vcategory')
admin.site.register(lecturevideo,lecturevideoAdmin)

# Register your models here.







