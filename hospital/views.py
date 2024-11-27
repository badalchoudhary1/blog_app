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


def edit_patient(request, patient_id):
    patient = get_object_or_404(Hospital, id=patient_id)
    
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        patient_disease = request.POST.get('patient_disease')

        if patient_name:
            patient.name = patient_name
        if patient_disease:
            patient.disease = patient_disease
        
        patient.save()
        
        return redirect('get_all_patient')
    
    context = {
        'patient_name': patient.name,
        'patient_disease': patient.disease
    }
    return render(request, 'edit_patient.html', context)
def delete_patient(request,patient_id):
    patient=get_object_or_404(Hospital,id=patient_id)
    patient.delete()
    return redirect('get_all_patient')


    




    



    

