
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Department, Doctor, Medicine
import json
from django.contrib.auth.decorators import login_required

@login_required
def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors = department.doctor_set.all()
    medicines = department.medicine_set.all()
    return render(request, 'Department/department_detail.html', {'department': department, 'doctors': doctors, 'medicines': medicines})

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'Department/department_list.html', {'departments': departments})

@login_required
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

@login_required
def doctor_detail_view(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'Department/doctor_detail.html', {'doctor': doctor})

@login_required
def index(request):
    departments = Department.objects.all()
    return render(request, 'Department/index.html', {'departments': departments})




@login_required
def index(request):
    # قائمة بجميع الأقسام
    departments = Department.objects.all()

    # تحويل قائمة الأقسام إلى شكل JSON
    departments_dict = {}
    for department in departments:
        department_doctors = list(Doctor.objects.filter(department=department).values())
        departments_dict[department.id] = department_doctors

    doctors_json = json.dumps(departments_dict)

    return render(request, 'Department/index.html', {'departments': departments, 'doctors_json': doctors_json})    







@login_required
def ABOUT(request):
    departments = Department.objects.all()
    return render(request, 'Department/ABOUT.html', {'departments': departments})   






@login_required
def Home_Services(request):
    departments = Department.objects.all()
    return render(request, 'Department/Home_Services.html', {'departments': departments})   






    


    







   








