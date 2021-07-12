from celery import shared_task

from apps.employee.models import Employee


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()


@shared_task
def Send_report():
    total = Employee.objects.all().count()
    send_mail(
        'Relatório',
        f'Relatório geral {total}',
        'To',
        ['From'],
        fail_silently=False,
    )
