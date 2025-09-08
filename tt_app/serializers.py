from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Timesheet, LineItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class TimesheetCreateRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    description = serializers.CharField()
    rate = serializers.FloatField()

    def create(self, validated_data):
        return Timesheet.objects.create(
            user_id=validated_data["user_id"],
            description=validated_data["description"],
            rate=validated_data["rate"]
        )


class LineItemCreateRequestSerializer(serializers.Serializer):
    timesheet_id = serializers.IntegerField()
    date = serializers.DateTimeField()
    minutes = serializers.IntegerField()

    def create(self, validated_data):
        return LineItem.objects.create(
            timesheet_id=validated_data["timesheet_id"],
            date=validated_data["date"],
            minutes=validated_data["minutes"]
        )


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ["id", "date", "minutes"]


class TimesheetSerializer(serializers.ModelSerializer):
    entries = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Timesheet
        fields = ["id", "description", "rate", "entries", "created_at"]