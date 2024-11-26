from django.shortcuts import render,redirect,get_object_or_404
from .models import Hospital
from django.http import HttpResponse

# Create your views here.
def create_patient(request):
    if request.method =='POST':
        name=request.POST.get('name')
        disease=request.POST.get('disease')

        Hospital.objects.create(name=name,disease=disease)
        return redirect("get_all_patient")
        
    else:
        return render(request,'add_patient.html')
def get_all_patient(request):
    x=Hospital.objects.all()
    return render(request,'get_all_patient.html',{"patients":x})

def get_patient(request,id):
    y= get_object_or_404(Hospital,id=id)
    return render(request,"get_patient.html",{"patient":y})




    



    

