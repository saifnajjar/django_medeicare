
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Department, Doctor, Medicine
import json




def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors = department.doctor_set.all()
    medicines = department.medicine_set.all()
    return render(request, 'Department/department_detail.html', {'department': department, 'doctors': doctors, 'medicines': medicines})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'Department/department_list.html', {'departments': departments})



def all_doctors(request):
    # قائمة بجميع الأقسام
    departments = Department.objects.all()

    # تحويل قائمة الأقسام إلى شكل JSON
    departments_dict = {}
    for department in departments:
        department_doctors = list(Doctor.objects.filter(department=department).values())
        departments_dict[department.id] = department_doctors

    doctors_json = json.dumps(departments_dict)

    return render(request, 'Department/all_doctors.html', {'departments': departments, 'doctors_json': doctors_json})


def doctor_detail_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'Department/doctor_detail.html', {'doctor': doctor})



def index(request):
    return render(request, 'Department/index.html')    


    


    







   








