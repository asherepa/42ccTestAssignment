from django.core.management.base import CommandError, NoArgsCommand
from django.db import models


class Command(NoArgsCommand):
    help = 'Print count of all models in project'

    def handle_noargs(self, **options):
        for m in models.get_models():
            if hasattr(m, 'objects'):
                model_count_line = "Models %s: %d" % (m._meta.app_label,
                                                      m.objects.count())
                self.stderr.write("error: %s" % model_count_line)
                self.stdout.write(model_count_line)
