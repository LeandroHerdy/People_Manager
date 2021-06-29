from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from apps.employee.models import Employee


class List_employee(ListView):
    model = Employee

    def get_queryset(self):
        logged_in = self.request.user.employee.company
        return Employee.objects.filter(company=logged_in)


class Update_employee(UpdateView):
    model = Employee
    fields = ['name', 'departament']


class Delete_employee(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employee')


class Create_employee(CreateView):
    model = Employee
    fields = ['name', 'departament']

    def form_valid(self, form):
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0] + employee.name.split(' ')[1]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(Create_employee, self).form_valid(form)   # 23
