from django.contrib import admin
from .models import ApplicationFormClass,Contact,Bhim_App, Quiz,Profile
# Register your models here.

class ApplicationFormClassAdmin(admin.ModelAdmin):
    list_display = ['date','firstName', 'lastName', 'date_of_birth', 'board', 'fatherName', 'motherName', 'qualification', 'schoolName', 'schoolAddress', 'homeAddress', 'state', 'aadharNumber', 'phoneNumber', 'emailID', 'username', 'referral', 'status', 'mail_sent']


admin.site.register(ApplicationFormClass, ApplicationFormClassAdmin)
admin.site.register(Contact)
admin.site.register(Bhim_App)
admin.site.register(Quiz)
admin.site.register(Profile)