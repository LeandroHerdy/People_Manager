from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.core.serializers import UserSerializer, GroupSerializer
from .tasks import Send_report


@login_required
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)

def Celery(request):
    Send_report.delay()
    return HttpResponse('Tarefa em execução.')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
