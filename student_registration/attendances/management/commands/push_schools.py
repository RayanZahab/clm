__author__ = 'achamseddine'

from django.core.management.base import BaseCommand

from student_registration.attendances.tasks import *


class Command(BaseCommand):
    help = 'Push Schools data to CouchBase'

    def handle(self, *args, **options):
        set_app_schools()