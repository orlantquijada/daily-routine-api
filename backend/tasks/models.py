from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from backend.utils import global_vars

from backend.users import models as user_models
from backend.tasks import managers


class Task(models.Model):
    of_user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=global_vars.TASK_TITLE_MAX_LENGTH)
    start_time = models.TimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)

    objects = managers.TaskManager()

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.of_user.full_name()} / {self.title}'

    def clean(self, *args, **kwargs):
        if self.start_time and not self.duration:
            raise ValidationError(_('Start time must have a duration.'))

        super().clean(*args, **kwargs)


class Record(models.Model):
    of_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_accomplished = models.BooleanField(default=False)

    objects = managers.RecordManager()

    def __str__(self):
        # pylint: disable=no-member
        is_accomplished = '/ Accomplished' if self.is_accomplished else ''
        return f'{self.of_task} / {self.date} {is_accomplished}'
