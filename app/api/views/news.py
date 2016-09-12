from datetime import datetime, date, timedelta, time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from api.serializers import news as news_serializers

from news.models import News


class NewsView(APIView):
    request_serializer_class = news_serializers.NewsRequestSerializer
    response_serializer_class = news_serializers.NewsResponseSerializer

    def get(self, request):
        """
        Новости
        ---
        parameters:
            - name: date_from
              required: False
              paramType: query
            - name: date_to
              required: False
              paramType: query

        serializer: api.serializers.news.NewsRequestSerializer
        """
        request_serializer = self.request_serializer_class(
            data=request.query_params
        )

        if not request_serializer.is_valid():
            return Response(
                {'success': False, 'errors': request_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        q_filter = Q()

        date_from = request_serializer.validated_data.get('date_from')
        date_to = request_serializer.validated_data.get('date_to')

        if date_from:
            q_filter &= Q(created__gte=date_from)

        if date_to:
            q_filter &= Q(created__lte=date_to)

        news = News.objects.filter(q_filter).order_by('id')

        response_serializer = self.response_serializer_class(news, many=True)
        return Response(response_serializer.data)

