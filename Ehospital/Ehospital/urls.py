"""
URL configuration for Ehospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login),
    path('logout/', views.user_logout),
    path('home/', views.homepage_view),
    path('addpatient/', views.addpatient_view),
    path('cnfuser/', views.confirmuser_view),
    path('adddiagnosis/', views.adddiagnosis_view),
    path('updatediagnosis/', views.updatediagnosis_view),
    path('cnfuser1/', views.confirmuser1_view),
    path('addbedadm/', views.addbedadmission_view),
    path('updbedadm/', views.updbedadmission_view),
    path('cnfuser2/', views.confirmuser2_view),
    path('patienthistory/', views.patienthistory_view),
    path('cnfuser3/', views.confirmuser3_view),
    path('patientbill/', views.patientbills_view),
    path('updatebill/', views.updatebills_view),
    path('help/', views.help_view),
]
