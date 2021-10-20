import csv

from django.core.management.base import BaseCommand
from school.models import HomeworkResult


class Command(BaseCommand):

    def handle(self, *args, **options):
        get_report(self)


def get_report(self):

    homework_results = HomeworkResult.objects.all()
    homework_results_list = []

    for homework_result in homework_results:
        homework_dict = {}
        homework_dict['student'] = f'{homework_result.student.firstname} \
                                     {homework_result.student.lastname}'
        homework_dict['teacher'] = f'{homework_result.teacher.firstname} \
                                     {homework_result.teacher.lastname}'
        homework_dict['created'] = homework_result.homework.created.strftime('%Y-%m-%d %H:%M')
        homework_results_list.append(homework_dict)

    keys = homework_results_list[0].keys()

    with open('homework-results.csv', 'w', newline='') as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys)
        dict_writer.writerows(homework_results_list)
