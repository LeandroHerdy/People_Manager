from django.views.generic import CreateView

from .models import Document


class Create_document(CreateView):
    model = Document
    fields = ['description', 'archive']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.created_by_id = self.kwargs['employee_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
