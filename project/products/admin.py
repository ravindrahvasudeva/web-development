from django.contrib import admin
from . models import people, Benifits, SurveyOfficer, Survey


class peopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone_number', 'Aadhar_no', 'RD_NO', 'salary', 'address', 'rationcard', 'cardtype')


class BenifitsAdmin(admin.ModelAdmin):
    list_display = ('rationcard', 'rice', 'dall', 'sugar')

class SurveyOfficerAdmin(admin.ModelAdmin):
    list_display = ('off_id', 'name', 'place', 'no_of_surveys')

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('off_id', 'rationcard')


admin.site.register(people, peopleAdmin)
admin.site.register(Benifits, BenifitsAdmin)
admin.site.register(SurveyOfficer, SurveyOfficerAdmin)
admin.site.register(Survey, SurveyAdmin)

