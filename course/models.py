from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=20)
    description = models.TextField()
    max_capacity = models.PositiveBigIntegerField()
    department = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
    pass_grade = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    assistant_trainer =models. CharField(max_length=20)
    tools = models.TextField()



    def __str__(self) -> str:
        return f"{self.course_name} {self.course_code}"
