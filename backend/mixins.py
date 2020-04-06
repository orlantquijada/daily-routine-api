from django.db import models
from backend.utils import global_vars


class NameMixin(models.Model):

    first_name = models.CharField(
        max_length=global_vars.NAME_MAX_LENGTH, blank=True, null=True)
    last_name = models.CharField(
        max_length=global_vars.NAME_MAX_LENGTH, blank=True, null=True)

    class Meta:
        abstract = True

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
