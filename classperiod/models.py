from django.db import models


class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=20)
    day_of_week = models.CharField(max_length=20)
   



    def __str__(self) -> str:
        return f"{self.start_time} {self.end_time}"
