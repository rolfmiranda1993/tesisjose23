from django.contrib import admin
from .models import StaffProfile, departamentoD


@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('staff_no', 'staff_name', 'designation', 'reporting_officer'
                    )

@admin.register(departamentoD)
class departamentoDAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'jerarquia'
                    )