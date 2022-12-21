from django.contrib import admin
from .models import StaffProfileD

# Register your models here.
@admin.register(StaffProfileD)
class StaffProfileDAdmin(admin.ModelAdmin):
    list_display = ('staff_no', 'staff_name', 'designation', 'reporting_officer'
                    )