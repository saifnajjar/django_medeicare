
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Department, Doctor, Medicine
import json
from django.contrib.auth.decorators import login_required
from .models import OpeningHours
from django.shortcuts import render, redirect
from .models import Department, Doctor

from django.shortcuts import render, redirect

from .models import Department, Doctor, OpeningHours, PatientBooking




def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors = department.doctor_set.all()
    medicines = department.medicine_set.all()
    opening_hours = OpeningHours.objects.all()
    
    return render(request, 'Department/department_detail.html', {'department': department, 'doctors': doctors, 'medicines': medicines, 'opening_hours': opening_hours })
    


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
    
    opening_hours = OpeningHours.objects.all()
    return render(request, 'Department/index.html', {'opening_hours':opening_hours})





from django.shortcuts import render, redirect
from .models import Department, OpeningHours, Doctor, PatientBooking

def index(request):
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('date1')
        notes = request.POST.get('note')

        try:
            department = Department.objects.get(pk=department_id)
            doctor = Doctor.objects.get(pk=doctor_id)
        except Department.DoesNotExist or Doctor.DoesNotExist:
            return redirect('index')

        booking = PatientBooking(
            patient_name=patient_name,
            phone_number=phone_number,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            notes=notes
        )
        booking.save()

        return redirect('index')

    else:
        departments = Department.objects.all()
        doctors = Doctor.objects.all()
        opening_hours = OpeningHours.objects.all()

        return render(request, 'Department/index.html', {
            'departments': departments,
            'doctors': doctors,
            'opening_hours': opening_hours,
        })

def get_doctors(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors = department.doctor_set.all().values('id', 'name')  # Get doctors associated with the selected department
    return JsonResponse(list(doctors), safe=False)






def ABOUT(request):
    departments = Department.objects.all()
    opening_hours = OpeningHours.objects.all()
    return render(request, 'Department/ABOUT.html', {'departments': departments,'opening_hours': opening_hours })   







def Home_Services(request):
    departments = Department.objects.all()
    opening_hours = OpeningHours.objects.all()
    return render(request, 'Department/Home_Services.html', {'departments': departments, 'opening_hours': opening_hours})  





   











    


    







   








