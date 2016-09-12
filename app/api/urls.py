from django.conf.urls import url, include

from api.views.news import NewsView

urlpatterns = [
    url(r'^news', NewsView.as_view()),
]
