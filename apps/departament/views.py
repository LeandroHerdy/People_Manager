from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.departament.models import Departament


class List_departament(ListView):
    model = Departament

    def get_queryset(self):
        logged_in = self.request.user.employee.company
        return Departament.objects.filter(company=logged_in)


class Create_departament(CreateView):
    model = Departament
    fields = ['name']

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.company = self.request.user.employee.company
        departament.save()
        return super(Create_departament, self).form_valid(form)


class Update_departament(UpdateView):
    model = Departament
    fields = ['name']


class Delete_departament(DeleteView):
    model = Departament
    success_url = reverse_lazy('list_departament')
