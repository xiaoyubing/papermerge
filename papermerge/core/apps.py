from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'papermerge.core'
    label = 'core'

    def ready(self):
        from papermerge.core import signals
        from papermerge.core import checks
