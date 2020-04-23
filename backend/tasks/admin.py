from django.contrib import admin

from backend.tasks import models


admin.site.register(models.Task)
admin.site.register(models.Record)