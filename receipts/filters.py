import django_filters

from .models import Patients


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Patients
        fields = '__all__'
        exclude = ['date_of_payment', 'date_due_payment']
