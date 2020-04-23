from datetime import date

from rest_framework import mixins, viewsets
from rest_framework.response import Response

from django.utils.timezone import timedelta

from backend.tasks import models, serializers

from backend.utils.week_converter import week_number_to_date_range


class TaskViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    # pylint: disable=no-member
    queryset = models.Task.objects
    serializer_class = serializers.base.TaskSerializer

    def get_queryset(self):

        queryset = self.queryset

        serializer = serializers.query.TaskQuerySerializer(
            data=self.request.query_params
        )

        if not serializer.is_valid():
            return queryset.all()

        user_id = serializer.validated_data.get('user_id', None)
        if user_id:
            queryset = queryset.of_user(user_id)

        return queryset.all()


class RecordViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    # pylint: disable=no-member
    queryset = models.Record.objects
    serializer_class = serializers.base.RecordSerializer

    def get_queryset(self):

        queryset = self.queryset

        serializer = serializers.query.RecordQuerySerializer(
            data=self.request.query_params
        )

        if not serializer.is_valid():
            return queryset.all()

        week_no = serializer.validated_data.get('week_no', None)
        start_of_week, end_of_week = week_number_to_date_range(week_no)
        if week_no:
            return queryset.filter_date_range(start_of_week, end_of_week).all()

        date = serializer.validated_data.get('date', None)
        auto_create = serializer.validated_data.get('auto_create', None)
        if date:
            queryset = queryset.date(date)

            if auto_create:
                tasks = models.Task.objects.of_user(self.request.user)

                newly_created_records_ids = []
                for task in tasks:
                    obj, created = models.Record.objects.get_or_create(
                        of_task=task, date=date)

                if created:
                    newly_created_records_ids.append(obj.id)

                created_records = models.Record.objects.filter(
                    id__in=newly_created_records_ids)

                queryset.union(created_records)

        return queryset.all()
