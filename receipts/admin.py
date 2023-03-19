from django.contrib import admin
from .models import Patients


@admin.register(Patients)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'amount_paid', 'date_of_payment','date_due_payment')
    pass


