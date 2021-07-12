from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from apps.overtime.forms import Registration_overtime_form
from apps.overtime.models import Overtime


class List_overtime(ListView):
    model = Overtime

    # translator
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_button'] = _("Employee report")
        return context

    def get_queryset(self):
        company_in = self.request.user.employee.company
        return Overtime.objects.filter(employee__company=company_in)


class Update_overtime(UpdateView):
    model = Overtime
    form_class = Registration_overtime_form

    def get_form_kwargs(self):
        Kwargs = super(Update_overtime, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs


class Update_overtime_base(UpdateView):
    model = Overtime
    form_class = Registration_overtime_form
    # success_url = reverse_lazy('list_overtime')

    def get_success_url(self):
        return reverse_lazy('update_overtime_base', args=[self.object.id])

    def get_form_kwargs(self):
        Kwargs = super(Update_overtime_base, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs


class Create_Overtime(CreateView):
    model = Overtime
    form_class = Registration_overtime_form

    def get_form_kwargs(self):
        Kwargs = super(Create_Overtime, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs


class Delete_overtime(DeleteView):
    model = Overtime
    success_url = reverse_lazy('list_overtime')
