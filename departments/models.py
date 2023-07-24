

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='department_images/', blank=True, null=True)

    def __str__(self):
        return self.name













class Doctor(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    degree = models.CharField(max_length=100, default='MD')
    availability = models.CharField(max_length=100, default='Monday to Friday')
    
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)  # Add the ImageField with upload_to parameter
    summary = models.TextField(default='No summary available')  # Set a default value for summary
    email = models.EmailField(default='example@example.com')
    phone_number = models.CharField(max_length=20, default='123456789')
    department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name



class Medicine(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name



class Education(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.description}" 



class PatientBooking(models.Model):
    patient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    appointment_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"               
