from django import forms
from .models import Patients
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class MyForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'second_name', 'amount_paid', 'date_of_payment', 'date_due_payment']
        labels = {'first_name': 'First Name', 'second_name': 'Second Name', 'amount_paid': 'Amount Paid',
                  'date_of_payment':'Date Paid', 'date_due_payment': 'Due Payment' }

