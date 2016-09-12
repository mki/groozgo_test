from datetime import date, timedelta, time, datetime

from django.utils import timezone

from rest_framework import serializers

from news.models import News


class NewsRequestSerializer(serializers.Serializer):
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)


class NewsResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'created')
