# coding=utf-8
import os
import subprocess

from django.core.management import BaseCommand, CommandError

_DEFAULTS__NEO4J_VERSION = '2.3.2'
_OPTION__NEO4J_VERSION = 'neo4j_version'

_DEFAULTS__DOCKER_DIR = '/usr/local/bin'
_OPTION__DOCKER_DIR = 'docker-dir'

_COMMAND__CREATE = 'create'
_COMMAND__DESTROY = 'destroy'
_COMMAND__RECREATE = 'recreate'
_COMMAND__START = 'start'
_COMMAND__STOP = 'stop'
_COMMAND__RESTART = 'restart'
_COMMAND__STATUS = 'status'
_COMMAND__LOG = 'log'


class Command(BaseCommand):
    help = 'Manages Neo4j Docker container for development/testing purposes.'

    args = '[{}]'.format('|'.join([
        _COMMAND__CREATE,
        _COMMAND__DESTROY,
        _COMMAND__RECREATE,
        _COMMAND__START,
        _COMMAND__STOP,
        _COMMAND__RESTART,
        _COMMAND__STATUS,
        _COMMAND__LOG,
    ]))

    missing_args_message = 'no command specified'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--neo4j-version',
            nargs='1',
            type=str,
            dest=_OPTION__NEO4J_VERSION,
            help='specify neo4j version [default={}]'.format(_DEFAULTS__NEO4J_VERSION),
            default=_DEFAULTS__NEO4J_VERSION,
        )
        parser.add_argument(
            '-d', '--docker-compose-dir',
            nargs='1',
            type=str,
            dest=_OPTION__DOCKER_DIR,
            help='specify docker binaries directory [default={}]'.format(_DEFAULTS__DOCKER_DIR),
            default=_DEFAULTS__DOCKER_DIR,
        )

        commands = parser.add_mutually_exclusive_group(required=True)

        commands.add_argument(
            'create',
            nargs='+',
            help='create the docker container',
        )
        commands.add_argument(
            'destroy',
            nargs='+',
            help='destroy the docker container',
        )
        commands.add_argument(
            'recreate',
            nargs='+',
            help='destroy and create the docker container',
        )
        commands.add_argument(
            'start',
            nargs='+',
            help='start the docker container',
        )
        commands.add_argument(
            'stop',
            nargs='+',
            help='stop the docker container',
        )
        commands.add_argument(
            'restart',
            nargs='+',
            help='restart the docker container',
        )
        commands.add_argument(
            'status',
            nargs='+',
            help='get the status of the docker container',
        )

    def handle(self, *args, **options):
        from django.conf import settings

        neo4j_version = options[_OPTION__NEO4J_VERSION]

        if len(args) != 1:
            raise CommandError('invalid arguments (see help)')

        neo4j_docker_dir = os.path.join(settings.BASE_DIR, 'docker', 'neo4j')
        if not os.path.isdir(neo4j_docker_dir):
            raise CommandError('neo4j docker settings directory does not exist: {}'.format(neo4j_docker_dir))

        docker_dir = options[_OPTION__DOCKER_DIR]
        docker = os.path.join(docker_dir, 'docker')
        if not os.path.isfile(docker):
            raise CommandError('docker command does not exist: {}'.format(docker))

        docker_compose = os.path.join(docker_dir, 'docker-compose')
        if not os.path.isfile(docker_compose):
            raise CommandError('docker-compose command does not exist: {}'.format(docker_compose))

        command_args_by_name = {}

        command_args_by_name[_COMMAND__CREATE] = [
            [
                docker,
                'run',
                '--rm',
                '--volume="{}/conf:/conf/'.format(neo4j_docker_dir),
                'neo4j:{}'.format(neo4j_version),
                'dump-config',
            ],
        ]

        command_args_by_name[_COMMAND__DESTROY] = [
            [docker_compose, 'kill'],
            [docker_compose, 'rm', '-f'],
        ]

        command_args_by_name[_COMMAND__RECREATE] = command_args_by_name[_COMMAND__DESTROY] + command_args_by_name[
            _COMMAND__CREATE]

        command_args_by_name[_COMMAND__START] = [
            [docker_compose, 'up', '-d'],
        ]

        command_args_by_name[_COMMAND__STOP] = [
            [docker_compose, 'stop'],
        ]

        command_args_by_name[_COMMAND__RESTART] = command_args_by_name[_COMMAND__STOP] + command_args_by_name[
            _COMMAND__START]

        command_args_by_name[_COMMAND__STATUS] = [
            [docker_compose, 'status'],
        ]

        command_args_by_name[_COMMAND__LOG] = [
            [docker_compose, 'logs'],
        ]

        command = args[0]
        command_args_list = command_args_by_name.get(command)
        if command_args_list is None:
            raise CommandError('unsupported command: {}'.format(command))

        for command_args in command_args_list:
            return_code = subprocess.call(command_args, cwd=neo4j_docker_dir)
            if return_code:
                raise CommandError('command failed with return code: {}'.format(return_code))

        self.stdout.write(
            self.style.SUCCESS('command "{}" executed successfully'.format(command))
        )
