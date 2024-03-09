from django.shortcuts import render
from app.forms import *

# Create your views here.
def djf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    return render(request,'djf.html',d)