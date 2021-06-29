from django.forms import ModelForm
from .models import Overtime
from apps.employee.models import Employee


class Registration_overtime_form(ModelForm):
    def __init__(self, user, *args, **Kwargs):
        super(Registration_overtime_form, self).__init__(*args, **Kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(company=user.employee.company)

    class Meta:
        model = Overtime
        fields = ['remark', 'employee', 'hour']
