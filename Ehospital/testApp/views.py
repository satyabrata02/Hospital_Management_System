from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from testApp.models import Patientinfo, Diagnosis, Patientbill, Patientbedadm
import datetime
# Create your views here.
def user_login(request):
    nfd = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('/home')
        else:
            nfd = 'Invalid Username and Password'
    return render(request, 'testapp/login.html',{'nfd':nfd})

def user_logout(request):
    logout(request)
    return redirect('/')

def homepage_view(request):
    return render(request,'testapp/index.html')

def addpatient_view(request):
    dt = datetime.datetime.now()
    if request.method == 'POST':
        pname = request.POST['pname']
        paddr = request.POST['paddr']
        pphno = request.POST['pphno']
        page = request.POST['page']
        pgender = request.POST['pgender']
        pbldgp = request.POST['pbldgp']
        pdisease = request.POST['pdisease']

        add_patient = Patientinfo(admissiondate=dt, pname=pname, address=paddr, phonenumber=pphno, age=page, gender=pgender, bloodgroup=pbldgp, disease=pdisease)
        add_patient.save()
        return redirect('/home')
    return render(request,'testapp/insertpatient.html')

def confirmuser_view(request):
    nfd = ''
    if request.method == 'POST':
        try:
            pid = request.POST['pid']
            pdata = Patientinfo.objects.get(patientid=pid)
            pname = pdata.pname
            pphno = pdata.phonenumber
            pdis = pdata.disease
            if pdata:
                request.session['pid'] = pid
                request.session['pname'] = pname
                request.session['pphno'] = pphno
                request.session['pdis'] = pdis
                pdata2 = Diagnosis.objects.filter(patientid=pid)
                if pdata2:
                    return redirect('/updatediagnosis')
                else:
                    return redirect('/adddiagnosis')
        except:
            nfd = 'Invalid Patient ID. Data not fount'
    return render(request,'testapp/patientconfirm.html',{'nfd':nfd})

def adddiagnosis_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    pdis = request.session['pdis']
    if request.method == 'POST':
        drname = request.POST['drname']
        symptoms = request.POST['psymptoms']
        pdig = request.POST['pdig']
        pmdcn = request.POST['pmdcn']
        paddm = request.POST['paddm']

        if symptoms.lower() == pdis.lower():
            pdis = symptoms
        elif symptoms == '':
            pdis = symptoms
        else:
            pdis = pdis+','+symptoms
        print(pdis)

        add_diagnosis = Diagnosis(patientid=pid, drname=drname, symptoms=pdis, diagnosis=pdig, medicines=pmdcn, addmissionreq=paddm)
        add_diagnosis.save()
        return redirect('/home')
    my_dict = {'pid':pid,'pname':pname,'pphno':pphno,'pdis':pdis}
    return render(request,'testapp/insertdiagnosis.html',my_dict)

def updatediagnosis_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    pdata = Diagnosis.objects.get(patientid=pid)
    drname = pdata.drname
    psymptoms = pdata.symptoms
    pdig = pdata.diagnosis
    pmdcn = pdata.medicines
    paddm = pdata.addmissionreq
    if request.method == 'POST':
        symptoms = request.POST['psymptoms']
        dign = request.POST['pdig']
        mdcn = request.POST['pmdcn']
        paddm = request.POST['paddm']


        if symptoms.lower() == psymptoms.lower():
            psymptoms = symptoms
        elif symptoms == '':
            psymptoms = pdata.symptoms
        else:
            psymptoms = psymptoms+','+symptoms

        if dign.lower() == pdig.lower():
            pdig = dign
        elif dign == '':
            pdig = pdata.diagnosis
        else:
            pdig = pdig+','+dign

        if mdcn.lower() == pmdcn.lower():
            pmdcn = mdcn
        elif mdcn == '':
            pmdcn = pdata.medicines
        else:
            pmdcn = pmdcn+','+mdcn

        upd_diagnosis = Diagnosis(patientid=pid, drname=drname, symptoms=psymptoms, diagnosis=pdig, medicines=pmdcn, addmissionreq=paddm)
        upd_diagnosis.save()
        return redirect('/home')
    my_dict = {'pid':pid,'pname':pname,'pphno':pphno,'pdata':pdata}
    return render(request,'testapp/updatediagnosis.html',my_dict)

def confirmuser1_view(request):
    nfd = ''
    if request.method == 'POST':
        try:
            pid = request.POST['pid']
            pdata = Patientinfo.objects.get(patientid=pid)
            pname = pdata.pname
            pphno = pdata.phonenumber
            pdata2 = Diagnosis.objects.get(patientid=pid)
            admreq = pdata2.addmissionreq
            if admreq == 'yes':
                request.session['pid'] = pid
                request.session['pname'] = pname
                request.session['pphno'] = pphno
                pdata3 = Patientbedadm.objects.filter(patientid=pid)
                if pdata3:
                    return redirect('/updbedadm')
                else:
                    return redirect('/addbedadm')
            else:
                nfd = 'Patient Bed Admission not Required.'
        except:
            nfd = 'Patient Bed Admission not Required.'
    return render(request,'testapp/patientconfirm.html',{'nfd':nfd})

def addbedadmission_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    dt = datetime.datetime.now()
    tnc = "The hospital shall not be held liable in the unfortunate event of a patient's demise, regardless of the cause or circumstances leading to such an occurrence."
    if request.method == 'POST':
        prelnames = request.POST['prelname']
        prelrelation = request.POST['relrelation']
        prephno = request.POST['prephoneno']
        proomno = request.POST['roomno']
        assignstf = request.POST['assignedstaffs']
        termsncond = request.POST['termsorcond']

        add_bedadm = Patientbedadm(patientid=pid, admitdate=dt, prelname=prelnames, relrelation=prelrelation, prephoneno=prephno, roomno=proomno, assignedstaffs=assignstf, termsorcond=termsncond)
        add_bedadm.save()
        return redirect('/home')
    my_dict = {'pid':pid,'pname':pname,'pphno':pphno,'tnc':tnc}
    return render(request,'testapp/bedadmission.html',my_dict)

def updbedadmission_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    pdata = Patientbedadm.objects.get(patientid=pid)
    dt = pdata.admitdate
    tnc = "The hospital shall not be held liable in the unfortunate event of a patient's demise, regardless of the cause or circumstances leading to such an occurrence."
    if request.method == 'POST':
        prelnames = request.POST['prelname']
        prelrelation = request.POST['relrelation']
        prephno = request.POST['prephoneno']
        proomno = request.POST['roomno']
        assignstf = request.POST['assignedstaffs']
        termsncond = request.POST['termsorcond']

        add_bedadm = Patientbedadm(patientid=pid, admitdate=dt, prelname=prelnames, relrelation=prelrelation, prephoneno=prephno, roomno=proomno, assignedstaffs=assignstf, termsorcond=termsncond)
        add_bedadm.save()
        return redirect('/home')
    my_dict = {'pid':pid,'pname':pname,'pphno':pphno,'pdata':pdata,'tnc':tnc}
    return render(request,'testapp/updbedadmission.html',my_dict)

def confirmuser2_view(request):
    nfd = ''
    if request.method == 'POST':
        try:
            pid = request.POST['pid']
            pdata = Patientinfo.objects.get(patientid=pid)
            if pdata:
                request.session['pid'] = pid
                return redirect('/patienthistory')
        except:
            nfd = 'Invalid Patient ID. Data not fount'
    return render(request,'testapp/patientconfirm.html',{'nfd':nfd})

def patienthistory_view(request):
    pid = request.session['pid']
    pdata = Patientinfo.objects.get(patientid=pid)
    try:
        pdata2 = Diagnosis.objects.get(patientid=pid)
    except:
        pdata2 = ''
    try:
        pdata3 = Patientbedadm.objects.get(patientid=pid)
    except:
        pdata3 = ''
    patient_info = {'pdata':pdata, 'pdata2':pdata2, 'pdata3':pdata3}
    return render(request,'testapp/patienthistory.html',patient_info)

def confirmuser3_view(request):
    nfd = ''
    if request.method == 'POST':
        try:
            pid = request.POST['pid']
            pdata = Patientinfo.objects.get(patientid=pid)
            pname = pdata.pname
            pphno = pdata.phonenumber
            pdata2 = Patientbedadm.objects.get(patientid=pid)
            if pdata2:
                request.session['pid'] = pid
                request.session['pname'] = pname
                request.session['pphno'] = pphno
                pbilldata = Patientbill.objects.filter(patientid=pid)
                if pbilldata:
                    return redirect('/updatebill')
                else:
                    return redirect('/patientbill')
        except:
            nfd = 'Invalid Patient ID. Data not fount'
    return render(request,'testapp/patientconfirm.html',{'nfd':nfd})

def patientbills_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    dt = datetime.datetime.now()
    if request.method == 'POST':
        totaldays = request.POST['days']
        pwardcharge = request.POST['wardcharge']
        pdrfee = request.POST['drfee']
        psrvcharge = request.POST['srvcharge']

        totalwardchg = eval(totaldays) * eval(pwardcharge)
        ptotalamt = eval(pdrfee) + eval(psrvcharge) + totalwardchg

        add_bills = Patientbill(patientid=pid, dischargedate=dt, days=totaldays, wardcharge=pwardcharge, drfee=pdrfee, srvcharge=psrvcharge, totalamt=ptotalamt)
        add_bills.save()
        return redirect('/updatebill')
    my_dict = {'pid':pid,'pname':pname,'pphno':pphno}
    return render(request,'testapp/patientbills.html',my_dict)

def updatebills_view(request):
    pid = request.session['pid']
    pname = request.session['pname']
    pphno = request.session['pphno']
    dt = datetime.datetime.now()
    pdata = totalwardchg = ptotalamt = dueamt = ''
    try:
        pdata = Patientbill.objects.get(patientid=pid)
        totalwardchg = pdata.days * pdata.wardcharge
        ptotalamt = pdata.drfee + pdata.srvcharge + totalwardchg
        dueamt = ptotalamt - pdata.paidamt
    except:
        print('Data not found')
    if request.method == 'POST':
        totaldays = eval(request.POST['days'])
        pwardcharge = eval(request.POST['wardcharge'])
        pdrfee = eval(request.POST['drfee'])
        psrvcharge = eval(request.POST['srvcharge'])
        ppaidamt = eval(request.POST['paidamt'])

        totalwardchg = totaldays * pwardcharge
        ptotalamt = pdrfee + psrvcharge + totalwardchg
        if ppaidamt == ptotalamt:
            ppayment = 'paid'
        else:
            ppayment = 'not paid'

        update_bills = Patientbill(patientid=pid, dischargedate=dt, days=totaldays, wardcharge=pwardcharge, drfee=pdrfee, srvcharge=psrvcharge, paidamt=ppaidamt, totalamt=ptotalamt, payment=ppayment)
        update_bills.save()
        return redirect('/updatebill')
    my_dict = {'pid':pid, 'pname':pname, 'pphno':pphno, 'pdata':pdata, 'totalwardchg':totalwardchg, 'ptotalamt':ptotalamt, 'dueamt':dueamt}
    return render(request,'testapp/updatebills.html', my_dict)

def help_view(request):
    return render(request,'testapp/help.html')
