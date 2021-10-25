import csv

from django.core.management.base import BaseCommand
from school.models import HomeworkResult


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_report(self)


def get_report() -> list:

    homework_results = HomeworkResult.objects.all()
    homework_results_list = []

    for homework_result in homework_results:
        homework_dict = {}
        homework_dict['student'] = str(homework_result.student)
        homework_dict['teacher'] = str(homework_result.teacher)
        homework_dict['created'] = homework_result.homework.created.strftime('%Y-%m-%d %H:%M')
        homework_results_list.append(homework_dict)
    return homework_results_list


def report_to_csv(report: list) -> None:
    keys = report[0].keys()
    with open('homework-results.csv', 'w', newline='') as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys)
        dict_writer.writerows(report)


def create_report(self):
    report = get_report()
    report_to_csv(report)
