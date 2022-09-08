from django.contrib import admin
from . models import people, SurveyOfficer



class peopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone_number', 'Aadhar_no', 'RD_NO', 'salary', 'address', 'rationcard', 'cardtype')




class SurveyOfficerAdmin(admin.ModelAdmin):
    list_display = ('off_id', 'name', 'place', 'no_of_surveys')



admin.site.register(people, peopleAdmin)

admin.site.register(SurveyOfficer, SurveyOfficerAdmin)


