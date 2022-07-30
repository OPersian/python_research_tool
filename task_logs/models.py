"""
Models layer.
"""
from django.contrib.auth.models import User as DjangoUser
from django.db import models


class CommonInfo(models.Model):
    """
    Common info for reuse by other models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


#class User(models.Model):
#    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)


class Task(CommonInfo):
    task_title = models.CharField(max_length=128)

    class Meta:
        db_table = "task"

    def __str__(self):
        return f"Task : {self.id}"


class DataType(CommonInfo):
    data_type_title = models.CharField(max_length=128)

    class Meta:
        db_table = "data_type"

    def __str__(self):
        return f"Data Type : {self.id}"


class TaskDataSize(CommonInfo):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

    DATA_SIZE_CHOICES = [
        (SMALL, "SMALL"),
        (MEDIUM, "MEDIUM"),
        (LARGE, "LARGE"),
    ]

    task_id = models.ForeignKey(Task, on_delete=models.RESTRICT)
    data_size_title = models.CharField(max_length=128, choices=DATA_SIZE_CHOICES)
    data_size_numeric = models.PositiveIntegerField()
    comment = models.TextField(null=True)  # e.g. elements in an array, dimensions in a matrix

    class Meta:
        db_table = "task_data_size"

    def __str__(self):
        return f"Data Size : {self.id}"


class Mode(CommonInfo):
    mode_title = models.CharField(max_length=128)

    class Meta:
        db_table = "mode"

    def __str__(self):
        return f"Mode : {self.id}"


class Cpu(CommonInfo):
    model_number = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=128)

    class Meta:
        db_table = "cpu"

    def __str__(self):
        return f"CPU : {self.id}"


class Log(CommonInfo):
    """
    Task execution results, or logs.
    """

    task_id = models.ForeignKey(Task, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(DjangoUser, on_delete=models.RESTRICT)
    data_type_id = models.ForeignKey(DataType, on_delete=models.RESTRICT)
    task_data_size_id = models.ForeignKey(TaskDataSize, on_delete=models.RESTRICT)
    mode_id = models.ForeignKey(Mode, on_delete=models.RESTRICT)
    cpu_id = models.ForeignKey(Cpu, on_delete=models.RESTRICT)
    measurable_start_time = models.DateTimeField(auto_now=True)
    measurable_end_time = models.DateTimeField(auto_now=True)
    duration_nano_sec = models.PositiveBigIntegerField(null=True)
    space_taken_bytes = models.PositiveBigIntegerField(null=True)

    class Meta:
        db_table = "log"

    def __str__(self):
        return f"Log : {self.id}"
