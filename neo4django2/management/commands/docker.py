# coding=utf-8
from django.core.management import BaseCommand

_OPTION__NEO4J_VERSION = 'neo4j_version'


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_option(
            '-n', '--neo4j-version',
            nargs='1',
            type=str,
            dest=_OPTION__NEO4J_VERSION,
        )

    def handle(self, *args, **options):
        options.get(_OPTION__NEO4J_VERSION, '2.3.2')
