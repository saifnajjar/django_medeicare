
from django.contrib import admin
from .models import Doctor, Medicine, Department
from .models import Doctor, Education
from .models import PatientBooking
from .models import OpeningHours

admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Department)
admin.site.register(Education)
admin.site.register(PatientBooking)
admin.site.register(OpeningHours)

