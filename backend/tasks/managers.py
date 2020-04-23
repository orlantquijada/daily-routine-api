from django.db import models


class TaskManager(models.Manager):

    def of_user(self, user_id):
        return self.filter(of_user=user_id)

    def has_duration(self):
        return self.filter(duration__is_null=False)

    def has_start_time(self):
        return self.filter(start_time__is_null=False)


class RecordManager(models.Manager):

    def filter_date_range(self, start_date, end_date):
        return self.filter(date__range=(start_date, end_date))

    def date(self, date):
        return self.filter(date=date)
