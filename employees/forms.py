from django import forms
from .models import Employee

# this form will be used for both the update and the create employee functionality
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'years_experience', 'department')

        labels = {
            'years_experience': ('years of experience')
        }
