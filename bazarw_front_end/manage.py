#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    deploy_mode()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def deploy_mode():

    mode = os.getenv('DEPLOY_MODE')
    print('mode: {0}'.format(mode))
    dev_settings = 'bazarw_front_end.deploy.default.settings'
    prod_settings = 'bazarw_front_end.deploy.prod.settings'
    prod = 'PROD'

    if mode is None:
        print('settins mode: DEFAULT')
        print('DJANGO_SETTINGS_MODULE: {0}'.format(dev_settings))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', dev_settings)

    if mode is None and mode == prod:
        print('settins mode: {0}'.format(prod))
        print('DJANGO_SETTINGS_MODULE: {0}'.format(prod_settings))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', prod_settings)

if __name__ == '__main__':
    main()
