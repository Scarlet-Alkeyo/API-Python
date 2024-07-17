from django.db import models

class Classroom(models.Model):
    class_name = models.CharField(max_length =20)
    class_code = models.CharField(max_length=20)
    assistant_trainer_incharge = models.CharField(max_length=20)
    room_number  = models.SmallIntegerField()
    class_rep = models.CharField(max_length=20)
    number_of_tables = models.SmallIntegerField() 
    number_of_seats= models.SmallIntegerField()
    max_number_seats = models.PositiveIntegerField()
    number_of_groups = models.PositiveIntegerField()




    def __str__(self) -> str:
        return f"{self.class_name} {self.class_code}"
