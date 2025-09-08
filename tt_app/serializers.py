from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Timesheet, LineItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ["id", "date", "minutes"]


class TimesheetSerializer(serializers.ModelSerializer):
    entries = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Timesheet
        fields = ["id", "description", "created_at", "entries"]