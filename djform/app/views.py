from django.shortcuts import render,HttpResponse
from app.models import*
from app.forms import *

# Create your views here.
def djf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        sname=request.POST.get('sname')
        sage=request.POST.get('sage')
        spassword=request.POST.get('spassword')
        gender=request.POST.get('gender')
        saddress=request.POST.get('saddress')
        cource=request.POST.get('cource')
        SO=Student(sname=sname,sage=sage,spassword=spassword,gender=gender,saddress=saddress,cource=cource)
        SO.save()
        return HttpResponse('Student Created Succesfully')

    return render(request,'djf.html',d)