from django.contrib import admin
from testApp.models import Patientinfo, Diagnosis, Patientbill, Patientbedadm
# Register your models here.
class PatientinfoAdmin(admin.ModelAdmin):
    list_display = ['admissiondate', 'patientid', 'pname', 'address', 'phonenumber', 'age', 'gender', 'bloodgroup', 'disease']

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['patientid', 'drname', 'symptoms', 'diagnosis', 'medicines', 'addmissionreq']

class PatientbillAdmin(admin.ModelAdmin):
    list_display = ['patientid', 'days', 'wardcharge', 'drfee', 'srvcharge', 'paidamt', 'totalamt', 'payment']

class PatientbedadmAdmin(admin.ModelAdmin):
    list_display = ['patientid', 'admitdate', 'prelname', 'prephoneno', 'roomno', 'assignedstaffs', 'termsorcond']

admin.site.register(Patientinfo, PatientinfoAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Patientbill, PatientbillAdmin)
admin.site.register(Patientbedadm, PatientbedadmAdmin)
