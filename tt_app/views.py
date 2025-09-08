import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status
from .models import Timesheet, LineItem
from .serializers import UserSerializer, TimesheetSerializer, LineItemSerializer, TimesheetCreateRequestSerializer, LineItemCreateRequestSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer


class TimesheetViewSet(viewsets.ModelViewSet):
    serializer_class = TimesheetSerializer

    def get_queryset(self):
        user_id = self.request.data["user_id"]
        return Timesheet.objects.filter(user_id=user_id)

    def create(self, request):
        serializer = TimesheetCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)


class LineItemViewSet(viewsets.ModelViewSet):
    serializer_class = LineItemSerializer

    def get_queryset(self):
        timesheet_id = self.request.data["timesheet_id"]
        return LineItem.objects.filter(timesheet_id=timesheet_id)

    def create(self, request, *args, **kwargs):
        serializer = LineItemCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
