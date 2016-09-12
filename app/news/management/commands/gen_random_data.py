import random
import time

from django.core.management.base import BaseCommand

from news.models import News


class Command(BaseCommand):

    def handle(self, *args, **options):
        self._gen_news()

    def _gen_news(self):
        print('Generate news')

        random.seed(time.time())

        for i in range(25):
            News.objects.create(
                title='title {}'.format(i),
                content='content {}'.format(i),
            )
